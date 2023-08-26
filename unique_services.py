"""
Script to get the list of unique services from the source q/a table
"""
import spacy
import pandas as pd

nlp = spacy.load("ru_core_news_lg")
df = pd.read_csv('source_table.csv')

# print(df['№ услуги'][0])
print(df.info())

"""
RangeIndex: 1011 entries, 0 to 1010
Data columns (total 6 columns):
 #   Column                           Non-Null Count  Dtype
---  ------                           --------------  -----
 0   № услуги                         1005 non-null   object
 1   Полное наименование услуги       1007 non-null   object
 2   Сокращенное наименование услуги  1007 non-null   object
 3   Теги по услуге                   881 non-null    object
 4   Вопрос                           1009 non-null   object
 5   Ответ                            1008 non-null   object
"""

services = pd.DataFrame(columns = ['n','name','short_name'])
service_names = df.iloc[:,1].unique()
for service_name in service_names:
    service_row = df.loc[(df['Полное наименование услуги'] == service_name) & (df['№ услуги'].isnull() == False) & (df['Сокращенное наименование услуги'].isnull() == False)]
    if service_row.shape[0] <= 0:
        continue
    services.loc[len(services)] = [service_row.iloc[0,0], service_row.iloc[0,1], service_row.iloc[0,2]]

services.to_csv('services.csv', index=False)
