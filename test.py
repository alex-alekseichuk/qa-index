import spacy
import pandas as pd
from annoy import AnnoyIndex

nlp = spacy.load("ru_core_news_lg")

df = pd.read_csv('source_table.csv')

fN = "№ услуги"
fName = "Полное наименование услуги"
fShortName = "Сокращенное наименование услуги"
fTags = "Теги по услуге"
fQuestion = "Вопрос"
fAnswer = "Ответ"

# Define dimensions of the word embeddings (300 for en_core_web_md)
embedding_dim = 300

# Create an Annoy index
annoy_index = AnnoyIndex(embedding_dim, 'angular')  # 'angular' similarity metric works well with cosine similarity


predefined_sentences = [
    "The cat is sleeping on the mat.",
    # ... (other sentences)
]

for idx, sentence in enumerate(predefined_sentences):
    sentence_embedding = nlp(sentence).vector
    annoy_index.add_item(idx, sentence_embedding)

# Build the index
annoy_index.build(10)  # Number of trees, can be adjusted for trade-off between speed and accuracy


target_sentence = "A furry cat is sleeping on the soft mat."
num_similar_sentences = 5

target_embedding = nlp(target_sentence).vector
similar_indices = annoy_index.get_nns_by_vector(target_embedding, num_similar_sentences)

similar_sentences = [predefined_sentences[idx] for idx in similar_indices]

for sentence in similar_sentences:
    print("Similar Sentence:", sentence)



