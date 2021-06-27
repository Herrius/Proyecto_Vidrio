# -*- coding: utf-8 -*-
#https://planetachatbot.com/construyendo-chatbot-simple-desde-cero-en-python-usando-nltk/

import nltk  
import random  
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#nltk.download('punkt') # first-time use only  
#nltk.download('wordnet') # first-time use only
    
lemmer = nltk.stem.WordNetLemmatizer()  #WordNet is a semantically-oriented dictionary of English included in NLTK.
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)  

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)  
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):     
    for word in sentence.split():   
        if word.lower() in GREETING_INPUTS:   
            return random.choice(GREETING_RESPONSES)
   
def LemTokens(tokens):  
    return [lemmer.lemmatize(token) for token in tokens]  
    
def LemNormalize(text):  
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
def procesar_corpus():
    #f=open('chatbot.txt','r',errors = 'ignore') #desarrollo
    path = os.path.dirname(os.path.realpath(__file__)) #produccion
    f=open(path +'/chatbot.txt','r',errors = 'ignore')  #produccion
    raw=f.read()
    raw=raw.lower()# converts to lowercase
    return raw   
    
def responseNLTK(user_response):   
    robo_response=''   
    
    raw = procesar_corpus()
    sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences   
    #word_tokens = nltk.word_tokenize(raw)# converts to list of words
    
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')  
    tfidf = TfidfVec.fit_transform(sent_tokens)   
    vals = cosine_similarity(tfidf[-1], tfidf)   
    idx = vals.argsort()[0][-2]   
    flat = vals.flatten()   
    flat.sort()   
    req_tfidf = flat[-2]
    #print(idx)
    
    #sent_tokens.remove(user_response)  
    
    if(req_tfidf==0):   
        robo_response=robo_response+"I am sorry! I don't understand you"   
    else:   
        robo_response = robo_response+sent_tokens[idx]   
    return robo_response
    
def inicio():   
    
    flag=True  
    print("ROBO: My name is Robo. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    while(flag==True):   
        user_response = input()   
        user_response=user_response.lower()   
        if(user_response!='bye'):   
            if(user_response=='thanks' or user_response=='thank you' ):   
                flag=False   
                print("ROBO: You are welcome..")   
            else:   
                if(greeting(user_response)!=None):   
                    print("ROBO: "+greeting(user_response))  
                else:   
                    print("ROBO: ",end="")   
                    print(responseNLTK(user_response))   
                     
        else:   
            flag=False   
            print("ROBO: Bye! take care..")

#inicio() 