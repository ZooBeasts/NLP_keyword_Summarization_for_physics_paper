import unittest
import os
from keywords.TextRank import TextRank
from Segmentation import seg

class TestTextRank(unittest.TestCase):
    def setUp(self):
        self.stop_words = set()
        with open('stop_words.txt', encoding='UTF-8') as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                self.stop_words.add(word)

    def test_textrank(self):
        print('test_textrank------------------')
        content = 'according to paper, metasurface is 2D periodic structure, ' \
                  'which can be designed to manipulate the nature of electromagnetic wave that dosen’t exist'
        textrank = TextRank()
        words = [word for word in seg.cut(content) if word not in self.stop_words]
        keywords = textrank.textrank(words, window_size=10)
        print(keywords)

if __name__ == '__main__':
    unittest.main()


