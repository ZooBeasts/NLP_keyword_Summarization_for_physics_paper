
'''
text rank (sentence split, sentence preprocess, word split, word preprocess, word filter,caculate weight,
rank, cosine similarity as weight, sentence as node)

MMR (Q,C,R) = argmax(lambda * sim(s, Q) - (1-lambda) * max sim(s, r)) redundancy

K means (skip thought, bert, cluster, in each cluster, find the most similar sentence to the centroid)

'''


import nltk
import numpy as np
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

content = '001.txt'

with open(content, 'r', encoding='utf-8') as files:
    content = files.readlines()
    content = ' '.join(content)


# first step: add stopword, can import from nltk, or open loacl file with specific words
with open('stopwords.txt', 'r', encoding='utf-8') as files:
    stopwords = files.readlines()
    stopwords = [word.strip() for word in stopwords]

# second step: split sentence
# def remove_punctuation(line):
#     rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
#     line = rule.sub(' ', line)
#     return line

def split_sentence(content):
    # content = remove_punctuation(content).lower()
    sentences = nltk.sent_tokenize(content)
    word_list = []
    for word in sentences:
        if word not in stopwords:
            word_list.append(word)
    return word_list

def split_word(content):
    # content = remove_punctuation(content).lower()
    word_list = nltk.word_tokenize(content)
    return word_list

sentences = split_sentence(content.lower())
all_sentence_words = [words for words in sentences if len(words)]
all_sentences = [''.join(words) for words in all_sentence_words]
print(all_sentences)



word_embedding = {}
with open('glove.6B.50d.txt', 'r', encoding='utf-8') as files:
    for line in files.readlines():
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype='float32')
        word_embedding[word] = vector


# test token
# all_vocab = {}
# for sent in all_sentence_words:
#     all_vocab.update(sent)
# print(all_vocab)

sentence_vector = []
for words in all_sentence_words:
    if len(words) != 0:
        v = sum((word_embedding.get(word, np.zeros((50,))) for word in words)) / (len(words) + 0.001)
    else:
        v = np.zeros((50,))
    sentence_vector.append(v)

print(len(sentence_vector), len(all_sentence_words))

sim_mat = np.zeros([len(all_sentence_words), len(all_sentence_words)])
for i in range(len(all_sentence_words)):
    for j in range(len(all_sentence_words)):
        if i != j:
            sim_mat[i][j] = cosine_similarity(sentence_vector[i].reshape(1,50), sentence_vector[j].reshape(1,50))[0,0] / len(all_sentence_words[i])

print('simlarity matrix: {} '.format(sim_mat.shape))

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph,alpha=0.9, max_iter=100,tol=1e-06)

sent_scores = sorted(((scores[i],s) for i,s in enumerate(all_sentences)), reverse=True)
sn = 10
for i in range(sn):
    print(sent_scores[i][1])