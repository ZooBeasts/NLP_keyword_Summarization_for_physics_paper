import math


class TFIDF(object):
    def __init__(self):
        self.idf = {}
        self.idf_median = 0



    def compute_tfidf(self,words):
        assert self.idf and self.idf_median

        tf = {}
        for word in words:
            tf[word] = tf.get(word, 0.0) + 1.0


        tfidf = {}
        for word in set(words):
            tfidf[word] = tf[word] / len(words) * self.idf.get(word, self.idf_median)

        tfidf = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)
        return tfidf




    def load_idf(self,idf_path, splitter = ' '):
        with open(idf_path, 'r', encoding='UTF-8') as f:
            for line in f:
                line = line.strip()
                if not line or len(line.split(splitter)) != 2:
                    continue
                term, idf = line.split(splitter)
                self.idf[term] = float(idf)
        self.idf_median = sorted(self.idf.values())[len(self.idf) // 2]


    def train_idf(self, seg_files ,output_file_name, splitter=' '):
        doc_count = 0

        for seg_file in seg_files:
            with open(seg_file, encoding='UTF-8') as f:
                for line in f:
                    line= line.strip()
                    if not line:
                        continue
                    doc_count += 1
                    words = set(line.split(splitter))
                    for word in words:
                        self.idf[word] = self.idf.get(word, 0.0) + 1.0

        with open(output_file_name, 'w', encoding='UTF-8') as f:
            for word, df in self.idf.items():
                self.idf[word] = math.log(doc_count / (df + 1.0))
                f.write('{}{}{}\n'.format(word, splitter, self.idf[word]))



