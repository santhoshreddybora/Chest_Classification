from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.model_trainer import Training
from CNNClassifier import logger

STAGE_NAME="MODEL TRAINER PIPELINE"
class ModelTrainerPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
    

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started...")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} finished")
    except Exception as e:
        raise e