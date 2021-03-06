#following workshop from
#https://www.youtube.com/watch?v=U8m5ug9Q54M


import pandas as pd

## Upload data from disk and convert csv to pandas DataFrame

print('-----------------------------------------------------------------')
print("Dowloading the CSV file containing records of Scottish MP speeches; converting to pandas dataframe.")
print('-----------------------------------------------------------------')

# LM: I will have a look at a way to set relative file paths in python
harvard = pd.read_csv (r'/Users/noemieclaret/Downloads/parlScot_parl_v1.1.csv')


#clean a bit: keep only rows where there is actually a speech and get rid of speakers that do not have a classified gender

speech_table=harvard[:][harvard["is_speech"]==1]
speech_table_gender_parlID=speech_table[:].dropna(axis=0, how='any', subset=["gender"])



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
    
    
def find_sent_speech(speech):
    speech_score=0
    i=0
    for sent in speech:
        score = 0
        for word in sent:
            try:
                score += sentimentScores[word]
                if speech_score>=0:
                    i+=10
            except:
                pass
        speech_score+=score
    speech_score+=i
    return speech_score
        
        
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
        
       
        
#stemming (not used for our own dictionary)

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

#sentiment analysis with the affin dictionary to practice (using https protocole, and modifying a bit the code from the DS105 workshop)



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
    i=0
    for sent in speech:
        score = 0
        for word in sent:
            try:
                score += sentimentScores[word]
                if speech_score>0:
                    i+=10
            except:
                pass
        speech_score+=score
    speech_score+=i
    return speech_score
        
        
        
        
        
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
        
        
        
# Using our own dictionary
                                              
#new dict
al_dict=[["feminism", "10"],["feminist", "10"],["patriarchy", "10"],["patriarchal", "10"],["sexism", "10"],["sexist", "10"],["misoginy", "10"],["misogynistic", "10"],["misandry", "10"],["misandrist", "10"],["misogynoir", "10"],["empowering", "10"],["empowerment", "10"],["action", "10"],[ "plan", "10"],["gender", "10"],["balance", "10"],["violence", "10"],["against", "10"],["bias", "10"],["equity", "10"],["equality", "10"],["gap", "10"],["pay", "10"],["gay", "10"],[ "roles", "7"],[ "role", "7"],["stereotypes", "7"],[ "stereotype", "7"],["menstrual", "20"],["hygiene", "10"],["pregnant", "15"], ["maternal","10"],["maternity", "10"],["sexual", "10"],["reproductive", "10"],["right", "10"], ["rights","10"],["abortions", "9"],["sex", "8"],["work", "10"], [ "workers", "8"],[ "discrimination", "10"],["women", "10"],["woman", "10"],["female", "10"],["females", "10"],["feminine", "9"],["girl", "10"],["girls", "10"],["sexual", "7"],["assaults", "7"],["assaults", "7"],["rapes", "7"],["rape", "7"],["domestic", "8"]]

#create a dicttionary from the list
sentimentScores_al = {}
al_words=[]
for lst in al_dict:
    i=0
    for term in lst:
        if len(lst)==2:
            if i==0:
                key=term
                i+=1
                affin
                al_words.append(term)
            else:
                score=term
                sentimentScores_al[key] = float(score)
                
            
#functon to find the score of a guven speech   

def find_score_speech_al(speech):
    speech_score=0
    for sentence in speech:
        score = 0
        for word in sentence:
            if word in al_words:
                score += sentimentScores_al[word]
        speech_score+=score
    return speech_score

#create new series in orginal pandas dataframe                                                
score_speeches=[] 
for blob in clean_speeches2:
    for speech in blob:
        speech_score=find_score_speech_al(speech)
        score_speeches.append(speech_score)


#find averages scores women/men to get overview of findings


speech_table_gender_parlID["scores"]=score_speeches


scores_women=speech_table_gender_parlID["scores"][speech_table_gender_parlID["gender"]=="F"]
avg_score_women=sum(scores_women)/len(scores_women)

    
scores_men=speech_table_gender_parlID["scores"][speech_table_gender_parlID["gender"]=="M"]
avg_score_men=sum(scores_men)/len(scores_men)  
        
        
        
