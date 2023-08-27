from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.data_transformation import DataTransformation


class DTPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()