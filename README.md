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
9. Update the index.html 

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


* After DVC pipeline is built and now we need create and follow below steps
Jenkinsfile,Dockerfile,.dockerignore and main.yaml

**IN jenkins file under continuous deployment section we need to replace Unbuntu machine IP and link of docker compose yaml you after pushing the docker-compose.yaml file we need to extract link by clicking on raw data.** 

* After that we need to create basic things in AWS like Iam user creation and ECR register(for storing docker image)and EC2 instance(for running jenkins and application)
We are creating 2 ec2 instances one for jenkins installation and running and another one for application running 
* In 1st ec2 instance we need to run jenkins.sh script one by one
we need to set elastic ip so every time we restart the jenkins same public address will be there
and in jenkins server we need to set below keys in 
ECR_REPOSITORY 
AWS_ACCOUNT_ID
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
and SSH key

* In 2nd EC2 instance we need to run ec2_setup.sh script one by one command 
we need to set elastic ip so every time we restart the machine same public address will be there
after that set below secrets key in github actions 
URL #jenkins url.
USER # jenkins user name.
TOKEN #API Token should be generated in jenkins.
JOBS  # jobs name which we have given in jenkins.

all set we can push changes to github and we can manually trigger jenkins workflow or you want to deploy automatically you can add below lines in place of 'on' in main.yaml 

on:
  push:
    branches: [main]