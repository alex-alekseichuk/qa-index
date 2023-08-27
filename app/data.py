import pandas as pd

dfData = pd.read_csv('./data/source_table.csv')

fN = "№ услуги"
fName = "Полное наименование услуги"
fShortName = "Сокращенное наименование услуги"
fTags = "Теги по услуге"
fQuestion = "Вопрос"
fAnswer = "Ответ"


def question_by_index(index):
    return dfData.loc[index, fQuestion]


def answer_by_index(index):
    return dfData.loc[index, fAnswer]


def record_by_index(index):
    return dict(dfData.loc[index, :])


dfServices = pd.read_csv('./data/services.csv')

dictServices = dict()

for i, record in enumerate(dfServices.to_dict(orient='records')):
    record['i'] = i
    dictServices[record['n']] = record
