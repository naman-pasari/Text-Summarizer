from src.TextSummarizer.pipeline.data_ingestion_pipeline import DIPipeline
from src.TextSummarizer.pipeline.data_validation_pipeline import DVPipeline
from src.TextSummarizer.pipeline.data_transformation_pipeline import DTPipeline
from src.TextSummarizer.pipeline.model_trainer_pipeline import MTPipeline
from src.TextSummarizer.pipeline.model_evaluation_pipeline import MEPipeline
from src.TextSummarizer.logger import *
from src.TextSummarizer.exception import *

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DIPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)




STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DVPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)



STAGE_NAME = "Data Transformation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DTPipeline()
   data_transformation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)



STAGE_NAME = "Model Trainer stage"
try: 
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   os.system(f'pip install --upgrade accelerate')
   os.system(f'pip uninstall -y transformers accelerate')
   os.system(f'pip install transformers accelerate')
   model_trainer = MTPipeline()
   model_trainer.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)




STAGE_NAME = "Model Evaluation stage"
try: 
   logging.info(f"*******************")
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = MEPipeline()
   model_evaluation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)