import unittest
from keywords.Keywords import Keyword


class TestKeyword(unittest.TestCase):


    def setUp(self):
        self.keywords = Keyword(" path ")

    def test_textrank(self):
        print('test_textrank------------------')
        title = ''
        content = 'Today is new day, I am very happy, good morning'
        for top_k in range(5):
            keywords = self.keyword.extract(title, content, top_k=2, method='textrank',with_weight=False)
            print(keywords)
            keywords = self.keyword.extract(title, content, method='textrank',with_weight=True)
            print(keywords)


    def test_tfidf(self):
        print('test_tfidf------------------')
        title = ''
        content = 'Today is new day, I am very happy, good morning'
        for top_k in range(5):
            keywords = self.keyword.extract(title, content, top_k=2, method='tfidf',with_weight=False)
            print(keywords)
            keywords = self.keyword.extract(title, content, method='tfidf',with_weight=True)
            print(keywords)


if __name__ == '__main__':
    unittest.main()

