from keywords.TFIDF import TFIDF
import unittest
import os



class TestKeyword(unittest.TestCase):
    def setUp(self):
        self.tfidf = TFIDF()
        self.seg_data_dir = r'C:/pythonProject/test/data/'
        self.idf_file_path = r'C:/pythonProject/test/idf.txt'

    def test_tf_idf(self):
        print('test_train_idf------------------')
        seg_files = ['{}/{}'.format(self.seg_data_dir, f) for f in os.listdir(self.seg_data_dir)]
        self.tfidf.train_idf(seg_files= seg_files, output_file_name= self.idf_file_path)

        print('test_load_idf------------------')
        words = ['waveguide']
        self.tfidf.load_idf(self.idf_file_path)
        result = self.tfidf.compute_tfidf(words)
        print(result)



if __name__ == '__main__':
    unittest.main()