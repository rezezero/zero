import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

# Downloads
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text
text = "Python is used for machine learning and text analysis."

# Tokenization
tokens = word_tokenize(text)
print(tokens)

# POS Tagging
print(pos_tag(tokens))

# Stopword Removal
stop = stopwords.words('english')

filtered = []

for word in tokens:
    if word.lower() not in stop:
        filtered.append(word)

print(filtered)

# Stemming
ps = PorterStemmer()

for word in filtered:
    print(ps.stem(word))

# Lemmatization
lm = WordNetLemmatizer()

for word in filtered:
    print(lm.lemmatize(word))

# TF-IDF
tfidf = TfidfVectorizer()

result = tfidf.fit_transform([text])

print(result.toarray())



"""
ASSIGNMENT 7 - Text Analytics

Problem Statement:
Perform:
- Tokenization
- Stopword removal
- Stemming


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text = "Data Science is very interesting"

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stopword removal
stop = stopwords.words('english')
filtered = [w for w in tokens if w.lower() not in stop]

print("Filtered Words:", filtered)

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered]

print("Stemmed Words:", stemmed)

"""