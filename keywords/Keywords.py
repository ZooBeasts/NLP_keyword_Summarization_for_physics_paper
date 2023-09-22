from keywords.TFIDF import TFIDF
from keywords.TextRank import Textrank

from keywords.pos_tagging import pos_tagging

ALLOW_POS = ('num','vn', 'verb', 'adjective', 'adverb', 'conjunction', 'pronoun')
METHOD = ('TFIDF', 'textrank')




def get_default_stop_words():
    stop_words = set()
    with open('C:/pythonProject/keywords/stopwords.txt', encoding='UTF-8') as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            stop_words.add(word)
    return frozenset(stop_words)


class Keyword(object):
    def __init__(self, idf_path, pos=pos_tagging().cut, stop_words=get_default_stop_words(), idf_splitter=' ',
                 allow_pos=ALLOW_POS):
        self._tfidf = TFIDF()
        self._pos = pos
        self._tfidf.load_idf(idf_path, idf_splitter)
        self._textrank = Textrank()
        self._stop_words = stop_words
        self._allow_pos = allow_pos

    @staticmethod
    def _check_input(**kwargs):
        if 'method' in kwargs:
            method = kwargs['method']
            assert method in METHOD, 'ensure method in {}'.format(METHOD)

        if 'title' in kwargs and 'content' in kwargs:
            title = kwargs['title']
            content = kwargs['content']
            assert title or content, 'ensure title and content is not empty'

    def extract(self, title, content, top_k=10, method='TFIDF', filter_stopword=True, min_word_len=1,
                with_weight=True):
        method = method.upper()
        self._check_input(title=title, content=content, method=method)

        words = []
        text = title + ' ' + content
        for word, pos in self._pos(text):
            if filter_stopword and word in self._stop_words \
                    or len(word) < min_word_len \
                    or pos in self._allow_pos \
                    or not word.strip():
                continue
            words.append(word)
        print(words)

        if method == 'TFIDF':
            keywords = self._extract_by_tfidf(words)
        elif method == 'textrank':
            keywords = self._extract_by_textrank(words)
        else:
            raise ValueError

        if not with_weight:
            keywords = [keyword for keyword, weight in keywords]

        return keywords[:top_k]

    def _extract_by_tfidf(self, words):
        keywords = self._tfidf.compute_tfidf(words)
        return keywords

    def _extract_by_textrank(self, words):
        keywords = self._textrank.textrank(words)
        return keywords

