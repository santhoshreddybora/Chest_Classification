# Chest_Disease_Classification_From_Chest_Images

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 

## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n chest python=3.8 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

Run below command in bash terminal for MLflow demo for experiment tracking.
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/santhoshreddybora/Chest_Disease_Classification.mlflow \
export MLFLOW_TRACKING_USERNAME=santhoshreddybora \
export MLFLOW_TRACKING_PASSWORD=6c55756a5f3978c955e4cc8b87c551a506b89be8 \
python script.py
```




### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag