import kagglehub
import os
import shutil
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        # Download dataset
        try:
            path = kagglehub.dataset_download("mohamedhanyyy/chest-ctscan-images")
            print("Initial download path:", path)
            
            # Create and copy to destination
            dest_path = Path(self.config.local_data_file)
            dest_path.mkdir(parents=True, exist_ok=True)
            
            # Copy files
            source_path = Path(path)
            if source_path.is_dir():
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
            else:
                shutil.copy2(source_path, dest_path)
            
            print("Files copied to:", dest_path)
            return str(dest_path)
        except Exception as e:
            raise e

