# NLP_keyword_extraction
## This is the practice section for keyword extraction for English and Chinese
### Using Own sentencesplitter.py to split sentences, still has some flaws, can use nltk or jiebe to improve, but not in this work. 21/09/23



## Development blog:

Stil error in textrank. added simple partofspeech pos_tagging.py. TFIDF can extract the correct keywords in length of 6. The result below is the keywords extracted from my paper. 22/09/23
![image](https://github.com/ZooBeasts/NLP_keyword_extraction/assets/75404784/beb96367-7e5e-4beb-8061-8473c030f045)


Problem with textrank, I don't know why show ValueError: max() arg is an empty sequence, and why pass empty to min and max, didn't pass the unitest. (Yet TFIDF is working perfectly. Will add LDA later on ) 21/09/23

