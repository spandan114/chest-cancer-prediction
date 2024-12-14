import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        self.class_labels = {
            0: "Adenocarcinoma",
            1: "Large Cell Carcinoma",
            2: "Normal",
            3: "Squamous Cell Carcinoma"
        }

    def predict(self):
        # Load the trained model
        model_path = os.path.join("artifacts", "training", "model.h5")  # Update if necessary
        model = load_model(model_path)
        print(f"Model loaded from {model_path}")

        # Prepare the image for prediction
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict the class
        predictions = model.predict(test_image)
        predicted_class = int(np.argmax(predictions, axis=1)[0])  # Convert NumPy int to Python int
        confidence = float(np.max(predictions))  # Convert NumPy float32 to Python float

        # Map prediction to label
        prediction_label = self.class_labels.get(predicted_class, "Unknown")
        print(f"Prediction: {prediction_label} (Confidence: {confidence:.2f})")

        return {
            "class": prediction_label,
            "confidence": confidence
        }
