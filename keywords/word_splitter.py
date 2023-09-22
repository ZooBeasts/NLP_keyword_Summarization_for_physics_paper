import math
import re


class Textsplitter(object):

    def __init__(self, stops='([, . ?!！；：" & &/ ;::\t \n \f])'):
        self.stops = stops
        self.re_split_sentence = re.compile(stops)

    def split_sentences_for_seg(self, content, max_len=512):
        sentence = []
        for sent in self.re_split_sentence.split(content):
            if not sent:
                continue

            for i in range(math.ceil(len(sent) / max_len)):
                sent_segment = sent[i * max_len:(i + 1) * max_len]
                sentence.append(sent_segment)

        return sentence


if __name__ == '__main__':
    with open('C:/pythonProject/test/data/data.txt', 'r', encoding='UTF-8') as f:
        content = f.readlines()
        content = ''.join(content)
        text_spliter = Textsplitter()
        content = text_spliter.split_sentences_for_seg(content)
        print('split sentence for seg\n')
        print(content)
        with open('../test/data/test_set1.txt', 'w', encoding='utf-8') as f:
            for content in content:
                # clean_content = [content for content in content if content != ' ']
                f.write(f"{content}")






