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


