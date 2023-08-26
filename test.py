from model import get_answers

question = "Какие документы предоставить при обращении представителя по детской карте?"
print(question)
print()

answers = get_answers(question)

for idx, answer in enumerate(answers):
    print(idx)
    print(answer)

