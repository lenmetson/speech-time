#following workshop from
#https://www.youtube.com/watch?v=U8m5ug9Q54M



import pandas as pd

df=pd.read_csv("/Users/noemieclaret/Desktop/feliz_navidad.csv")

#convert each speech into lower case

lower_case_speeches=[]
def to_lower_case_speech(speech):
    for speech in csv['speech']:
        for word in speech:
            speech_lower=[]
            speech_lower.append(str.lower(word))
        lower_case_speeches.append(speech)
        

#tokenize
from nltk import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')


def tokenize_sent_speech(speech):
    sent_tok=[]
    for sent in speech:
        sent=sent.tokenize(sent)
        sent_tok.append(sent)
        return sent_tok
        
def tokenize_words_from_sentence(sent_tok):
    words_tok=[]
    for sentences in sent_tok:
        tokens = word_tokenize(sentences)
        words_tok.append(tokens)
        
#remove weird characters
import re

def remove_weird_characters(speech):
    sent_tok=tokenize_sent_speech(speech)
    clean_speech1=[]
    for sentence in sent_tok:
        clean_sentence=[]
        words_tok=tokenize_words_from_sentence(sentence)
        for tokens in words_tok:
            clean=[]
            for w in tokens:
                res=re.sub(r'[^\w\s]', "", w)
                if res!="":
                    clean.append(res)
            clean_sentence.append(clean)
        clean_speech.append(clean_sentence)
        
    
        
       
        
#remove stopwords


nltk.download('stopwords')
from nltk.corpus import stopwords
         
def remove_stopwords(clean_speech1):
    clean_speech2=[]
    for sentence in speech:
        t=[]
        for token in sentence:
            if not token in stopwords.words('english'):
                t.append(token)
        clean_speech2.append(t)
        
        
        
        
#stemming

from nltk.stem.porter import PorterStemmer   
port=PorterStemmer()   

def stem_speech(clean_speech2):
    clean_speech3=[]
    for sentence in clean_speech2:
        stemmed_tokens=[port.stem(i) for i in sentence]
        clean_speech3.append(stemmed_tokens)
        
        
        
        
        
#part 2
import nltk

import requests

response = requests.get("https://raw.githubusercontent.com/julioadl/ds101/master/nlp_workshop/AFINN_english.txt")
data = response.text
f=open('/Users/noemieclaret/Desktop/AFINN_english.txt',"w+")
f.write(data)



affin = f
sentimentScores = {}

for line in affin:
	term, score = line.split("\t")
	sentimentScores[term] = float(score)


sentences=["I am happy today", "I am sad today"]


newsSentiment = []

for sent in sentences:
	score = 0
	for word in sent:
		try:
			score += sentimentScores[word]
		except:
			pass
	if score > 0:
		sentiment = 'positive'
	elif score < 0:
		sentiment = 'negative'
	else:
		sentiment = 'neutral'
	s = ''.join(sent)
	newsSentiment.append([s, sentiment])
        
        
