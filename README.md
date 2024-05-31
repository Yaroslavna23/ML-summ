# ML web service on FastAPI

This repository contains the files to build your own Machine Learning web application! 

In this example is used summarising model from Hugging Face Hub.  

## Local development

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
env/Scripts/Activate.ps1 

# Install/upgrade dependencies
pip install -U -e .
pip install -U -e .[dev]

# (Optional) Code formatting
make pretty

# Run tests for ml code
make test_ml

# Run app
uvicorn app.app:app --host 0.0.0.0 --port 8080

# Deactivate the virtual environment
deactivate
``

## Run app in docker container

```bash
docker build -t ml-app .
docker run -p 80:80 ml-app
```

## Run tests for the app 

Run the following commands while docker container is running (in other terminal).

```bash
source env/bin/activate
make test_app

deactivate
```
