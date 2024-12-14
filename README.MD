Activate env
source cancer_prediction_env/bin/activate

dvc init
dvc repro
dvc dag