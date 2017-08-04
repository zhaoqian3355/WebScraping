from nltk import word_tokenize
from nltk import Text

tokens=word_tokenize("Here are some not very interesting text!")
text=Text(tokens)

print(text)