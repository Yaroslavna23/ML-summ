# ML web service on FastAPI

This repository contains the files to build your own Machine Learning web application! 

In this example is used summarising model from Hugging Face Hub.  

## Local development

```bash
# Create a virtual environment
python3.11 -m venv env

# Activate the virtual environment
source env/bin/activate

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
![URL](https://github.com/Yaroslavna23/ML-summ/assets/129892006/7ba4097a-9dbf-46ed-a790-a1cb6ccdda28)
![WEB-app]((https://github.com/Yaroslavna23/ML-summ/assets/129892006/9afd7c9d-de6a-4963-9d35-60d4dcc6cb5)

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
