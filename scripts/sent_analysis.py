#following workshop from
#https://www.youtube.com/watch?v=U8m5ug9Q54M


import pandas as pd

## Upload data from disk and convert csv to pandas DataFrame

print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')

# LM: I will have a look at a way to set relative file paths in python
harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')


#clean a bit

speech_table=harvard[:][harvard["is_speech"]==1]
speech_table_gender_parlID=speech_table[:][speech_table["gender"]==("F" or "M")].dropna(axis=0, how='any', subset=["type"])


#tokenize
from nltk import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')


#tokenize sentences for each speech

def tokenize_sent_speech(speech):
    sent_tok=[]
    for sent in speech:
        sent=sent_tokenize(sent)
        sent_tok.append(sent)
        return sent_tok

speeches_as_sentences=[]
for discours in speech_table_gender_parlID['speech']:
    speech=[discours]
    speech_tok_sent=tokenize_sent_speech(speech)
    speeches_as_sentences.append(speech_tok_sent)
    
    
#tokenize words

def tokenize_words_from_sentence(sentence):
    words_tok=[word_tokenize(i) for i in sentence]
    return words_tok
        
speeches_as_words=[]
for discours in speeches_as_sentences:
    sentences_as_words=[]
    for sentence in discours:
        sentence=tokenize_words_from_sentence(sentence)
        sentences_as_words.append(sentence)
    speeches_as_words.append(sentences_as_words)
    
# change to lower case    
    
    
def to_lower_case_speech(speech):
    speech_lower=[]
    for sentences in speech:
        for sentence in sentences:
            sentence_lower=[]
            for word in sentence:
                sentence_lower.append(str.lower(word))
            speech_lower.append(sentence_lower)
    return speech_lower
        
        
speeches_aswords_lower=[]          
for speech in speeches_as_words:
    lowercase_speech=to_lower_case_speech(speech)
    speeches_aswords_lower.append(lowercase_speech)
        
#remove weird characters
    
import re

def remove_weird_characters(speech):
    clean_speech1=[]
    clean_sentence=[]
    for sentence in speech:
        clean=[]
        for w in sentence:
            res=re.sub(r'[^\w\s]', "", w)
            if res!="":
                clean.append(res)
        clean_sentence.append(clean)
    clean_speech1.append(clean_sentence)
    return clean_speech1

                
clean_speeches1=[]            
for speech in speeches_aswords_lower:
    speech_no_weird=remove_weird_characters(speech)
    clean_speeches1.append(speech_no_weird)
            
           
       
        
#remove stopwords


nltk.download('stopwords')
from nltk.corpus import stopwords
         
def remove_stopwords(speech):
    clean_speech2=[]
    for sentence in speech:
        t=[]
        for token in sentence:
            if not token in stopwords.words('english'):
                t.append(token)
        clean_speech2.append(t)
    return clean_speech2
    
clean_speeches2=[]            
for speech in clean_speeches1:
    speech_rmv_stopwords=remove_stopwords(speech)
    clean_speeches2.append(speech_rmv_stopwords)
        
       
        
#stemming

from nltk.stem.porter import PorterStemmer   
port=PorterStemmer()   

def stem_speech(speech):
    clean_speech3=[]
    for sentences in speech:
        for sentence in sentences:
            stemmed_tokens=[port.stem(i) for i in sentence]
            clean_speech3.append(stemmed_tokens)
    return clean_speech3

clean_speeches3=[]
for speech in clean_speeches2:
    speech_stemmed=stem_speech(speech)
    clean_speeches3.append(speech_stemmed)
        
        
        
        
        
#part 2
import nltk

import requests

response = requests.get("https://raw.githubusercontent.com/julioadl/ds101/master/nlp_workshop/AFINN_english.txt")
data = response.text
data2=data.splitlines(keepends=False)

affin=[]
for i in data2:
    data_new=data.split()
    affin.append(data_new)




affin=[]
for i in data2:
    data_new=i.split()
    affin.append(data_new)
    
    
sentimentScores = {}
for lst in affin:
    i=0
    for term in lst:
        if len(lst)==2:
            if i==0:
                key=term
                i+=1
            else:
                score=term
                sentimentScores[key] = score
        elif len(lst)==3:
            if i==0:
                key1=term
                i+=1
            elif i==1:
                key2=term
                i+=1
            else:
                score=term
                sentimentScores[key1+" " +key2]=score


def find_sent_speech(speech):
    speech_score=0
    for sent in speech:
        score = 0
        for word in sent:
            try:
                score += sentimentScores[word]
            except:
                pass
        speech_score+=score
        
        
        
        
        
score_speeches=[] 
for speech in clean_speeches2:
    speech_score=find_score_speech(speech)
    score_speeches.append(speech_score)



#analyse


speech_table_gender_parlID["scores"]=score_speeches


scores_women=speech_table_gender_parlID["scores"][speech_table_gender_parlID["gender"]=="F"
avg_score_women=sum(scores_women)/len(scores_women)

    
scores_men=speech_table_gender_parlID["scores"][speech_table_gender_parlID["gender"]=="M"
avg_score_men=sum(scores_men)/len(scores_men)     
        
        
        
        
        
        
        
        
        
        
        
