## Keyword extraction for short physics letters, using TFIDF. Extractive summarization will use Textrank and Abstractive summarization will use a pre-trained model and further apply to QA chatbot 28/09/23
## More details that changed plz see Development_blog.txt


The task changed, so this project will apply NLTK to split sentences and words to achieve better results. 
Networkx package is used for textrank since self-written textrank.py has an issue returning an empty list.



## Development blog:
added text summarization Maximal Marginal Relevance(MMR) 28/09/23


Texkrank summarization is uploaded and useable for extracting BBC news dataset: https://www.kaggle.com/datasets/pariza/bbc-news-summary. self-written textrank.py works for Chinese, not sure why in English it returns an empty list, will continue investigating. Word_embedding is used glove.6b.50d.txt.https://www.kaggle.com/datasets/adityajn105/glove6b50d (28/09/23)
![image](https://github.com/ZooBeasts/NLP_keyword_Summarization_for_physics_paper/assets/75404784/cf9bff88-ea98-45c9-8e7f-79cad3796194)

Seems that nltk separates few flaws, but still able to extract 4 important words. 27/09/23 (end, problem solved for M, caused by not lower() the content)
![image](https://github.com/ZooBeasts/NLP_keyword_extraction/assets/75404784/edc0b317-1a97-465a-abdf-0a163a48d6dc)

Stil error in textrank. added simple partofspeech pos_tagging.py. TFIDF can extract the correct keywords in a length of 6. The result below is the keywords extracted from my paper. 22/09/23
![image](https://github.com/ZooBeasts/NLP_keyword_extraction/assets/75404784/beb96367-7e5e-4beb-8061-8473c030f045)


Problem with textrank, I don't know why show ValueError: max() arg is an empty sequence, and why pass empty to min and max, didn't pass the unitest. (Yet TFIDF is working perfectly. Will add LDA later on ) 21/09/23

