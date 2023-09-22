import unittest
from keywords.Keywords import Keyword
import keywords.word_splitter as Textsplitter
import numpy as np
class TestKeyword(unittest.TestCase):


    def setUp(self):
        self.keywords = Keyword('C:/pythonProject/test/idf.txt')

    # def test_textrank(self):
    #     print('test_textrank------------------')
    #     title = ''
    #     content = 'Today is new day, I am very happy, good morning'
    #     for top_k in range(5):
    #         keywords = self.keyword.extract(title, content, top_k=2, method='textrank',with_weight=False)
    #         print(keywords)
    #         keywords = self.keyword.extract(title, content, method='textrank',with_weight=True)
    #         print(keywords)


    def test_tfidf(self):
        print('test_tfidf------------------')
        title = ''
        with open ('C:/pythonProject/test/data/data2.txt','r',encoding='UTF-8') as f:
            content = f.readlines()
            content = ''.join(content)
            content = Textsplitter.Textsplitter().split_sentences_for_seg(content)
            content = ''.join(content)

            for top_k in range(6):
                keywords = self.keywords.extract(title, content, top_k=6, method='TFIDF', with_weight=False)
                print(keywords)
                print('------------------\n')
                keywords = self.keywords.extract(title, content, top_k=6, method='TFIDF', with_weight=True)
                print(keywords)

            for i in keywords:
                print(i[0])




if __name__ == '__main__':
    unittest.main()

