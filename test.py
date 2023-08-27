from app.data import *
from app.model import *
from app.classificator import *

# question = "Какие документы предоставить при обращении представителя по детской карте?"
question = "Какие документы нужны для получения паспорта?"
print(question)
print()

# qa = Qamodel()
# print('model init...')
# qa.init()
# print("done.")

# print(qa.predict_service(question))

# records = qa.get_records(question)
# for record in records:
#     print("N", record[fN])
#     print("Short", record[fShortName])
#     print("Name", record[fName])
#     print("Q.", record[fQuestion])
#     print()

print("init...")
labels = [dictServices[n] for _, n in dfData.loc[:, fN].items() if n in dictServices]

clServicesModel, clServicesVec = class_create(
    [value for _, value in dfData.loc[:, fQuestion].items()],
    labels,
)
print("done.")

prediction = class_predict(clServicesModel, clServicesVec, question)
print(prediction)
