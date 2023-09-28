
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
from sklearn.preprocessing import MinMaxScaler

title = ' empty title'
content = '001.txt'

with open(content, 'r', encoding='utf-8') as files:
    content = files.readlines()
    content = ' '.join(content)


# first step: add stopword, can import from nltk, or open loacl file with specific words
with open('stopwords.txt', 'r', encoding='utf-8') as files:
    stopwords = files.readlines()
    stopwords = [word.strip() for word in stopwords]

word_embedding = {}
with open('glove.6B.50d.txt', 'r', encoding='utf-8') as files:
    for line in files.readlines():
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], dtype='float32')
        word_embedding[word] = vector

# adding important words, based on the domain knowledge
important_words = set()
VIP_words = 'important_words.txt'
with open(VIP_words, 'r', encoding='utf-8') as files:
    for line in files.readlines():
        word = line.strip()
        important_words.add(word)

# second step: split sentence
# def remove_punctuation(line):
#     rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
#     line = rule.sub(' ', line)
#     return line

def split_sentence(content):
    sentences = nltk.sent_tokenize(content)
    word_list = []
    for word in sentences:
        if word not in stopwords:
            word_list.append(word)
    return word_list

def split_word(content):
    word_list = nltk.word_tokenize(content)
    return word_list


def vector(words):
    words = [words for words in words if words in word_embedding]
    words_vector = np.mean([word_embedding[word] for word in words], axis=0)  \
        if words else np.zeros(50)
    return words_vector

def get_sentence_vector(all_sentence_words):
    sentence_vec = np.array([vector(words) for words in all_sentence_words])
    return sentence_vec


def get_title_similarity(sentence_vec,title_vec):
    sim_mat = cosine_similarity(sentence_vec, title_vec)
    return sim_mat

def get_title_common_score(all_sentence_words, title_words):
    set_title_score = set(title_words)
    ret = []
    for words in all_sentence_words:
        set_words = set(words) & set_title_score
        if len(set_words) >= 3:
            ret.append(1.5)
        else:
            ret.append(1)
    return np.array(ret)

def get_position_score(sen_length):
    position_score = np.ones(sen_length)
    position_score[:3] = 2
    position_score[-3:] = 1.5
    return position_score

def have_importance_words(sentences):
    for entity in important_words:
        if entity in sentences:
            return 1
    return 0

def get_entities_score(sentence):
    vip_score = have_importance_words(sentence)
    return 1.5 if vip_score > 0 else 1

def get_clue_score(sentence):
    clue_words = 'anyway, in conclusion, in summary, to sum up, in short, in brief, to conclude, overall'
    result = []
    for sent in sentence:
        flag =1
        for word in clue_words:
            if word in sent:
                flag = 1.4
                break
        result.append(flag)
    return np.array(result)




def calculate_textrank(sentence_vec):
    sim_mat = cosine_similarity(sentence_vec)
    np.fill_diagonal(sim_mat, 0)
    nx_graph = nx.from_numpy_array(sim_mat)
    tol = 1e-6
    max_iter = 1000
    Flag = True
    while Flag:
        try:
            pagetrank_score = nx.pagerank(nx_graph, max_iter=max_iter, tol=tol)
            Flag = False
        except nx.PowerIterationFailedConvergence as e :
            print(e)
            tol *= 10

    pagetrank_score = np.array([v for k, v in sorted(pagetrank_score.items(), key=lambda x: x[0])])
    return pagetrank_score
    # Flag = True
    # while Flag:
    #     try:
    #         pagetrank_score = nx.pagerank(nx_graph, max_iter=max_iter, tol=tol)
    #         Flag = False
    #     except nx.PowerIterationFailedConvergence as e :
    #         print(e)
    #         tol *= 10



sentences = split_sentence(content.lower())
all_sentence_words = sentences
sentence_vec = get_sentence_vector(all_sentence_words)


pagetrank_score = calculate_textrank(sentence_vec)

entities_score = np.array([get_entities_score(sentence) for sentence in sentences])


title_words = split_sentence(title)
title_vec = get_sentence_vector(title_words)
title_sim_score = get_title_similarity(sentence_vec, title_vec)

title_common_score = get_title_common_score(all_sentence_words, title_words)

scaler = MinMaxScaler((1,2))
scaler.fit(title_sim_score)
title_sim_score = scaler.transform(title_sim_score)[:,0]

position_score = get_position_score(len(sentences))
clue_score = get_clue_score(sentences)

title_common = False
score = pagetrank_score *(title_common_score if title_common else title_sim_score) * position_score * clue_score * entities_score


extract_num = 10
n = extract_num
summary_set = []
alpha = 0.8
max_score_index = np.argmax(score)
summary_set.append(max_score_index)

while n >0:
    sim_mat = cosine_similarity(sentence_vec,sentence_vec[summary_set])
    sim_mat = np.max(sim_mat, axis=1)


    scaler = MinMaxScaler()
    feature_score = np.array([score,sim_mat]).T
    scaler.fit(feature_score)

    feature_score = scaler.transform(feature_score)
    [score, sim_mat] = feature_score[:,0],feature_score[:,1]

    mmr_score = alpha*score - (1-alpha)*sim_mat

    mmr_score[summary_set] = -100
    max_index = np.argmax(mmr_score)
    summary_set.append(max_index)

    n -= 1
print('------------------')

summary = [sen for idx, sen in enumerate(sentences) if idx in summary_set]
summary = ''.join(summary)
print(f'Summarization: {summary}')

print('------------------')

feature_score = pd.DataFrame({k:v for v,k in zip([score,pagetrank_score,entities_score,title_sim_score,title_common_score,position_score,clue_score,sentences],['score','pagetrank_score','entities_score','title_sim_score','title_common_score','position_score','clue_score','sentences'])})
feature_score.to_csv('feature_score.csv', index=False)
print(feature_score)



