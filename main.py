from src.Text_Summarizer.logging import logger
from src.Text_Summarizer.pipeline.stage1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"Stage {STAGE_NAME} initiated.")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e