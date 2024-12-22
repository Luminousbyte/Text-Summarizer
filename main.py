from src.Text_Summarizer.logging import logger
from src.Text_Summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Text_Summarizer.pipeline.stage2_data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated.")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try: 
    logger.info(f"Stage {STAGE_NAME} initiated.")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e