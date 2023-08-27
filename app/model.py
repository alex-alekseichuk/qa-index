import spacy
import pandas as pd
from annoy import AnnoyIndex
from .data import *
from .nlp import *
from .ann_index import *
from .classificator import *


class Qamodel:
    def init(self):
        self.annQuestions = create_ann_index([value for _, value in dfData.loc[:, fQuestion].items()])

        # self.clServicesModel, self.clServicesVec = class_create(
        #     [value for _, value in dfData.loc[:, fQuestion].items()],
        #     [dictServices[n] for _, n in dfData.loc[:, fN].items()])

    def predict_service(self, question):
        class_predict(self.clServicesModel, self.clServicesVec, question)

    def get_records(self, question):
        return get_records(self.annQuestions, question, 10)

    def get_first_answer(self, question):
        answers = get_answers(self.annQuestions, question)
        return answers[0]
