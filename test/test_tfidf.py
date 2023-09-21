from keywords.TFIDF import TFIDF
import unittest
import os



class TestKeyword(unittest.TestCase):
    def setUp(self):
        self.tfidf = TFIDF()
        self.seg_data_dir = 'C:/Users/pythonProject/test/data'
        self.idf_file_path = 'C:/Users/pythonProject/test/idf.txt'

    def test_tf_idf(self):
        print('test_train_idf------------------')
        seg_files = ['{}/{}'.format(self.seg_data_dir, f) for f in os.listdir(self.seg_data_dir)]
        self.tfidf.train_idf(seg_files= seg_files, output_file_name= self.idf_file_path)

        print('test_load_idf------------------')
        words = ['me', 'you', 'he', 'she', 'it', 'they', 'us', 'them']
        self.tfidf.load_idf(self.idf_file_path)
        result = self.tfidf.compute_tfidf(words)
        print(result)



if __name__ == '__main__':
    unittest.main()