from CNNClassifier import logger
from src.CNNClassifier.utils.common import read_yaml
logger.info("demo.py logging")

try:
    read_yaml("E:\Vscode\MLOPS-1\Chest_Disease_Classification\config\config.yaml")
except Exception as e:
    logger.info(e)