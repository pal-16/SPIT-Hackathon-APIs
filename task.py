import spacy
sp = spacy.load('en_core_web_sm')
import nltk
import json
from nltk.stem.porter import *
from flask import jsonify
stemmer = PorterStemmer()

def get_data(msg):
    msgSpacy = sp(msg)
    data = list(msgSpacy.ents)
    location,time,date,status='','','',''
    for word in data:
        print(word,word.label_)
        if word.label_ == 'GPE':
            location = str(word)
        elif word.label_ == 'TIME':
            time = str(word)
        elif word.label_ == 'DATE':
            date = str(word)
    for word in msgSpacy:
        text = stemmer.stem(str(word))
        if text=='accept' or text=='success':
            status = 1
        elif text=='cancel' or text=='declin' or text=='reject':
            status = 0
    print(location,time,date,status)
    send_data = {
        "location":location,
        "time":time,
        "date":date,
        "status":status 
    }
    return jsonify(send_data)