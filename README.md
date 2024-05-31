## ML web service on FastAPI


In this example is used summarising model from Hugging Face Hub.  

## Local development

```bash
# Create a virtual environment
python -m venv env

# Activate the virtual environment
.\env\Scripts\activate

# Install/upgrade dependencies
pip install -r .\ML-summ\requirements.txt
pip install -r .\ML-summ\requirements-dev.txt


## (Optional) Code formatting
#make pretty нету комманды MAKE в cmd и powershell
#
## Run tests for ml code
#make test_ml нету комманды MAKE в cmd и powershell

# Run app
uvicorn app.app:app --host 0.0.0.0 --port 8080

# Deactivate the virtual environment
deactivate
```

## Run app in docker container

```bash
docker build -t ml-app .
docker run -p 80:80 ml-app
или
docker-compose up
```

## Run tests for the app 

Run the following commands while docker container is running (in other terminal).

```bash
.\env\Scripts\activate
pytest

deactivate
```
