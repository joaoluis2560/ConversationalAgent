import nltk



# pos tagging using NLTK
def parts_of_speech(query_sentence):
    sentences = nltk.sent_tokenize(query_sentence)
    tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
    pos_tags = [nltk.pos_tag(sentence) for sentence in tokenized]
    print(pos_tags[0])

    

