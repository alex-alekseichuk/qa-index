# QA index

Install dependency:

```
pipenv install
pipenv shell
python -m spacy download ru_core_news_lg
```

Run dev. server locally:
```
uvicorn main:app --reload
```

Open Swagger web UI: `http://localhost:8000/docs`


Used libs:
- pandas
- spacy NLP
- annoy ANN
- FastAPI HTTP server


Shared notebook:

https://deepnote.com/workspace/sudo-df68-db5e6b1b-f096-429d-ac8f-752981730ddc

