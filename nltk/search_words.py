import nltk



with open('NLTK.txt', 'rb') as file:
    read_file = file.read().decode(errors='replace')
    text = nltk.Text(nltk.word_tokenize(read_file))
    match = text.concordance('language')
