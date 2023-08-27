from src.TextSummarizer.config.configuration import ConfigurationManager
from src.TextSummarizer.conponents.model_evaluation import ModelEvaluation

class MEPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()