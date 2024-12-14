import os
from dotenv import load_dotenv
import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.common import save_json

# Load environment variables from .env file
load_dotenv()

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.model = tf.keras.models.load_model("artifacts/training/model.h5")

        # Setup MLflow
        mlflow_uri = os.getenv('MLFLOW_TRACKING_URI')
        mlflow.set_tracking_uri(mlflow_uri)



    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

        
    def log_into_mlflow(self, project_name="chest-cancer-classification"):
        try:
            # Ensure the MLflow URI and credentials are correctly set
            print("Setting MLflow tracking URI:", os.environ.get("MLFLOW_TRACKING_URI"))
            mlflow.set_tracking_uri(os.environ.get("MLFLOW_TRACKING_URI"))
            
            print("Tracking URI set to:", mlflow.get_tracking_uri())
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            
            mlflow.set_experiment(project_name)
            with mlflow.start_run():
                print("MLflow run started.")
                
                # Log parameters
                print("Logging parameters:", self.config.all_params)
                mlflow.log_params(self.config.all_params)
                
                # Log metrics
                print("Logging metrics: Loss =", self.score[0], "Accuracy =", self.score[1])
                mlflow.log_metrics(
                    {"loss": self.score[0], "accuracy": self.score[1]}
                )
                
                # Log model
                if tracking_url_type_store != "file":
                    print("Registering model to MLflow server...")
                    mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
                    print("Model registered successfully.")
                else:
                    print("Logging model to file store...")
                    mlflow.keras.log_model(self.model, "model")
                    print("Model logged successfully.")
                    
        except Exception as e:
            print("MLflow Logging Error:", e)

