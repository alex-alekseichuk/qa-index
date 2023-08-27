# QA index

This is NLP model with HTTP interface for AI search against FAQ knowledge base.
It needs to use some linux box with `pyenv` and `pipenv` python tools already installed.

Install dependency locally:

```
pipenv install
pipenv shell
python -m spacy download ru_core_news_lg
```

Run dev. server locally:
```
uvicorn app.main:app --reload
```

## Build docker image and run locally:

Extracting dependencies directly from Pipfile.lock
if your pipenv environment IS NOT synchronized (all packages are installed)
```
jq -r '.default
        | to_entries[]
        | .key + .value.version' \
    Pipfile.lock > requirements.txt
```

```
docker build -t qa-index-server .
docker run -ti --rm --name qa-index-server -p8000:8000 qa-index-server
```

Open Swagger web UI: `http://localhost:8000/docs`

