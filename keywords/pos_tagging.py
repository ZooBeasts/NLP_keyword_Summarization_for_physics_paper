# Define a function for custom part-of-speech tagging
import nltk
import re

class pos_tagging(object):
    
    @staticmethod
    def cut_nltk(sentence):
        stops = '([，。？, . ?!！；：";::\t \\n [] ])'
        sentence = re.sub(r'[^\w]', ' ', sentence)

        token_word = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(token_word)

        return tagged_words




    
    @staticmethod
    def cut(sentence):
        words = sentence.split()
        tagged_words = []

        for word in words:
            if word.endswith("ed"):
                tagged_words.append((word, "verb"))
            elif word.endswith("ing"):
                tagged_words.append((word, "verb"))
            elif word.endswith("ly"):
                tagged_words.append((word, "adverb"))
            elif word.endswith("s") or word.endswith("es") or word.endswith("ies"):
                tagged_words.append((word, "noun"))
            elif word.endswith("e") or word.endswith("or"):
                tagged_words.append((word, "noun"))
            elif word.endswith("able") or word.endswith("ible"):
                tagged_words.append((word, "adjective"))
            elif word.endswith("ion") or word.endswith("tion") or word.endswith("ation") or word.endswith("ition"):
                tagged_words.append((word, "noun"))
            elif word.endswith("er") or word.endswith("or"):
                tagged_words.append((word, "noun"))
            elif word.endswith("al") or word.endswith("ial"):
                tagged_words.append((word, "adjective"))
            elif word.endswith("ic") or word.endswith("tic"):
                tagged_words.append((word, "adjective"))
            elif word.endswith("ism"):
                tagged_words.append((word, "noun"))
            elif word.endswith("and") or word.endswith("but") or word.endswith("if") \
                    or word.endswith("while") or word.endswith("although") or word.endswith("though") \
                    or word.endswith("because") or word.endswith("since") or word.endswith("unless") \
                    or word.endswith("until") or word.endswith("whereas") or word.endswith("where") \
                    or word.endswith("after") or word.endswith("before") or word.endswith("once") \
                    or word.endswith("lest") or word.endswith("till") or word.endswith("when") \
                    or word.endswith("whenever") or word.endswith("wherever") or word.endswith("whether") \
                    or word.endswith("while") or word.endswith("until") or word.endswith("since") \
                    or word.endswith("so") or word.endswith("than") or word.endswith("that") \
                    or word.endswith("though") or word.endswith("till") or word.endswith("unless") or word.endswith("forward"):
                tagged_words.append((word, "conjunction"))
            elif word.endswith('1') or word.endswith('2') or word.endswith('3') or word.endswith('4') \
                    or word.endswith('5') or word.endswith('6') or word.endswith('7') or word.endswith('8') \
                    or word.endswith('9') or word.endswith('0'):
                tagged_words.append((word, "num"))
            elif word.endswith("the") or word.endswith("a") or word.endswith("an") or word.endswith("this") \
                or word.endswith("that") or word.endswith("these") or word.endswith("those") \
                or word.endswith("my") or word.endswith("your") or word.endswith("his") \
                or word.endswith("her") or word.endswith("its") or word.endswith("our") \
                or word.endswith("their") or word.endswith("few") or word.endswith("little") \
                or word.endswith("much") or word.endswith("many") or word.endswith("lot") \
                or word.endswith("most") or word.endswith("some") or word.endswith("any") \
                or word.endswith("enough") or word.endswith("all") or word.endswith("both") \
                or word.endswith("half") or word.endswith("either") or word.endswith("neither") \
                or word.endswith("each") or word.endswith("every") or word.endswith("other") \
                or word.endswith("another") or word.endswith("such") or word.endswith("what") \
                or word.endswith("rather") or word.endswith("quite") or word.endswith("as") \
                or word.endswith("as if") or word.endswith("as though") or word.endswith("when") \
                or word.endswith("than") or word.endswith("whether") or word.endswith("before") \
                or word.endswith("after") or word.endswith("till") or word.endswith("until") \
                or word.endswith("since") or word.endswith("while") or word.endswith("once") \
                or word.endswith("as long as") or word.endswith("so that") or word.endswith("unless") \
                or word.endswith("lest") or word.endswith("whereas") or word.endswith("where") \
                or word.endswith("wherever") or word.endswith("now that") or word.endswith("provided") \
                or word.endswith("only if") or word.endswith("even if") or word.endswith("in case") \
                or word.endswith("in the event that") or word.endswith("so as to") or word.endswith("so that") \
                or word.endswith("in order to") or word.endswith("that") or word.endswith("who") \
                or word.endswith("whom") or word.endswith("which") or word.endswith("whose") \
                or word.endswith("whoever") or word.endswith("whatever") or word.endswith("whichever") \
                or word.endswith("whomever") or word.endswith("whosever") or word.endswith("whatever") \
                or word.endswith("when") or word.endswith("whenever") or word.endswith("where") \
                or word.endswith("wherever") or word.endswith("why") or word.endswith("how") \
                or word.endswith("however") or word.endswith("whatever") or word.endswith("wherever") \
                or word.endswith("input") or word.endswith("howsoever") or word.endswith("whence") \
                or word.endswith("whither") or word.endswith("whence") or word.endswith("thither") \
                or word.endswith("hence") or word.endswith("thence") or word.endswith("whensoever") \
                or word.endswith("whenever") or word.endswith("wherever") or word.endswith("wheresoever") \
                or word.endswith("howsoever") or word.endswith("how") or word.endswith("why") \
                or word.endswith("what") or word.endswith("which") or word.endswith("who"):
                tagged_words.append((word, "pronoun"))

            else:
                tagged_words.append((word, "unknown"))

        return tagged_words


# Perform custom part-of-speech tagging
if __name__ == '__main__':
    with open('C:/pythonProject/test/data/test_set1.txt', 'r', encoding='UTF-8') as f:
        content = f.readlines()
        content = ''.join(content)
        tagged_words = pos_tagging.cut(content)
        with open('C:/pythonProject/test/data/pos_test_set1.txt', 'w', encoding='utf-8') as f:
            for word, pos in tagged_words:
                f.write((f"{word} {pos}  \n"))
