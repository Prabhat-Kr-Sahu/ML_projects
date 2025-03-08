import os
import sys

from src.exceptions import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.utils import save_object
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

'''The @dataclass decorator in Python is used to automatically generate special methods for a class, such as:

__init__() for initialization
__repr__() for a human-readable representation
__eq__() for comparison
Other utility methods (e.g., __hash__() if needed)
Why Use @dataclass?
Less Boilerplate Code: You don't need to manually write an __init__ method.
Automatic Initialization: Fields are automatically initialized with type hints and default values.
Readability: The class is more readable and maintainable, especially for configuration and data storage purposes.
'''

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv") 
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        '''
            This method initializes an instance of DataIngestion class
            DataIngestionConfig are initiated with default values
        '''

        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion methods Starts")
        try:
            df= pd.read_csv(r'D:\ML\src\components\raw_data\stud.csv')
            logging.info("Read the dataset as dataframe")
           
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True) 
            
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path, raw_data_path = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    