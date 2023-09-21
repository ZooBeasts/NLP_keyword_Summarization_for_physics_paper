import math
import re


class Textsplitter(object):

    def __init__(self, stops='([，。？, . ?!！；：";::\t \\n [] ])'):
        self.stops = stops
        self.re_split_sentence = re.compile(stops)



    def split_sentences_for_seg(self, content, max_len=512):
        sentence = []
        for sent in self.re_split_sentence.split(str(content)):
            if not sent:
                continue
            # elif sent.isdigit:
            #     continue
            for i in range(math.ceil(len(sent) / max_len)):
                sent_segment = sent[i * max_len:(i+1)*max_len]
                sentence.append(sent_segment)

        return sentence




if __name__ == '__main__':

    with open('data.txt','r',encoding='UTF-8') as f:
        content = f.readlines()
        text_spliter = Textsplitter()

        print('split sentence for seg\n')
        # for i, sent in enumerate(text_spliter.split_sentences_for_seg(content)):
        #     print('sent {} {}'. format(i, sent))
        test_set = []
        new = text_spliter.split_sentences_for_seg(content)
        test_set.append(new)
        with open('test_set.txt', 'w', encoding='utf-8') as f:
            f.write(str(test_set).strip('[]').replace(',', '').replace("'", '').replace('"[', ''))






