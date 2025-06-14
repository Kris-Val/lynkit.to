```sh
pre-commit install
python -m pip install -r requirements.txt -r requirements-dev.txt
uvicorn lynkitto.asgi:application --port 8000 --reload
```
