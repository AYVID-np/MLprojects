from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import os
from src.logger import logging 
from src.exception import CustomException
import pandas as pd
import sys
from src.components.data_transformation import DataTransformationConfig, DataTransformation
from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

@dataclass
class DataIngestionConfig:
    """ Provides input to data ingestion component """
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    """This function is responsible for data ingestion from data sources"""
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() 

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion component")

        try:
            df = pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Train Test Split initiated')

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is complete")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_path, test_path = obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_arr, test_arr,_ = data_transformation_obj.initiate_data_transformation(train_path,test_path)

    model_trainer_obj = ModelTrainer()
    r2_square_best_model = model_trainer_obj.initiate_model_trainer(train_arr, test_arr)
    print(r2_square_best_model)