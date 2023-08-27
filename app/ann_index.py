import spacy
import pandas as pd
from annoy import AnnoyIndex
from .data import *
from .nlp import *


def create_ann_index(questions):
    # Define dimensions of the word embeddings (300 for en_core_web_md)
    embedding_dim = 300

    # Create an Annoy index
    annoy_index = AnnoyIndex(embedding_dim, 'angular')  # 'angular' similarity metric works well with cosine similarity

    # question_pairs = [(index, value) for index, value in dfData.loc[:, fQuestion].items()]
    # for idx, question in question_pairs:
    for idx, question in enumerate(questions):
        # print(idx)
        # print(question)
        question = str(question)
        sentence_embedding = nlp(question).vector
        annoy_index.add_item(idx, sentence_embedding)

    # Build the index
    annoy_index.build(10)  # Number of trees, can be adjusted for trade-off between speed and accuracy

    return annoy_index


def get_answers(annoy_index, target_sentence):
    num_similar_sentences = 5

    target_embedding = nlp(target_sentence).vector
    similar_indices = annoy_index.get_nns_by_vector(target_embedding, num_similar_sentences)

    similar_sentences = [answer_by_index(index) for index in similar_indices]

    # for sentence in similar_sentences:
    #     print("Similar Sentence:", sentence)

    return similar_sentences


def get_records(annoy_index, target_sentence, num_similar_sentences=5):
    target_embedding = nlp(target_sentence).vector
    similar_indices = annoy_index.get_nns_by_vector(target_embedding, num_similar_sentences)

    similar_sentences = [record_by_index(index) for index in similar_indices]

    return similar_sentences
