from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum=0
    for word,value in wordList.items():
        sum+=value
    return sum

def retrieveRandomWord(wordList):

    randIndex=randint(1,wordListSum(wordList))
    for word,value in wordList.items():
        randIndex-=value
        if randIndex<=0:
            return word

def buildWordDict(text):
    