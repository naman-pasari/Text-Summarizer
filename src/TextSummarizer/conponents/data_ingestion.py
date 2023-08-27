import os
import shutil
import zipfile
from src.TextSummarizer.utils.common import logging
from src.TextSummarizer.entity import (DataIngestionConfig)




class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def import_file(self):
        if not os.path.exists(self.config.local_data_file):
            shutil.copy(self.config.source, self.config.local_data_file)
            logging.info(f"File copied to {self.config.local_data_file}")
        else:
            logging.info(f"File already exists in destination: {self.config.local_data_file}")  

        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)