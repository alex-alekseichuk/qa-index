from .model import *

# question = "Какие документы предоставить при обращении представителя по детской карте?"
question = "Какие документы нужны для получения паспорта?"
print(question)
print()

qa = Qamodel()
print('model init...')
qa.init()
print("done.")


qa.get_answer(question)
answers = get_answers(question)

for idx, answer in enumerate(answers):
    print(idx)
    print(answer)
