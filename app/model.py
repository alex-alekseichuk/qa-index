import spacy
import pandas as pd
from annoy import AnnoyIndex
from .data import *
from .nlp import *
from .ann_index import *


class Qamodel:
    def init(self):
        self.ann = create_ann_index()

    def get_answers(self, question):
        returnget_answers(self.ann, question)

    def get_first_answer(self, question):
        answers = get_answers(self.ann, question)
        return answers[0]
