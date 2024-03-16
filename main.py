from CNNClassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from CNNClassifier import logger
from CNNClassifier.pipeline.prepare_base_model_pipeline import PrepareBaseModelPipeline
from CNNClassifier.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from CNNClassifier.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>>>Stage {STAGE_NAME} started<<<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME="Prepare Base Model"
try:
    logger.info(f">>>>>>>Stage {STAGE_NAME} started<<<<<<<<<")
    obj=PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="MODEL TRAINER PIPELINE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started...")
    obj=ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished")
except Exception as e:
    raise e


STAGE_NAME="Evaluation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started...")
    obj=ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} finished")
except Exception as e:
    raise e