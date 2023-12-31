FROM python:3.10.7
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download ru_core_news_lg
COPY ./app /code/app
COPY ./data /code/data
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
