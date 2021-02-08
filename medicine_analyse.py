import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
import pickle
import numpy as np
from tensorflow.keras.models import load_model
model=load_model('Medicin_Model.h5')
import json
import random

intents=json.loads(open('medicine_intents.json').read())
words=pickle.load(open('medicine_words.pkl','rb'))
classes=pickle.load(open('medicine_classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
def bow(sentence,words):
    sentence_output=clean_up_sentence(sentence)
    bag=[0]*len(words)
    for s in sentence_output:
        for i,w in enumerate(words):
            if w==s:
                bag[i]=1
    return(np.array(bag))

def predict_information(sentence,model):
    tagr=()
    p=bow(sentence,words)
    output=model.predict(np.array([p]))[0]
    threshold=0.25
    result=[[i,r] for i,r in enumerate(output) if r>threshold]
    result.sort(key=lambda x: x[1],reverse=True)
    return_list=[]
    answer=[]
    for r in result:
        return_list.append({"intent":classes[r[0]],'probability':str(r[1])})
        for intent in intents['intents']:
            if classes[r[0]]==intent['tag']:
                answer=(random.choice(intent['responses']))
                tagr=intent['tag']
                # print(f"Alexa: {answer}")
                return answer
def predict_usage(sentence,model):
    tagr=[]
    p=bow(sentence,words)
    output=model.predict(np.array([p]))[0]
    threshold=0.25
    result=[[i,r] for i,r in enumerate(output) if r>threshold]
    result.sort(key=lambda x: x[1],reverse=True)
    return_list=[]
    answer=[]
    for r in result:
        return_list.append({"intent":classes[r[0]],'probability':str(r[1])})
        for intent in intents['intents']:
            if classes[r[0]]==intent['tag']:
                answer=(random.choice(intent['responses']))
                tagr=intent['tag']
                # print(f"Alexa: {answer}")
                return tagr
# while True:
#     try:
#         a=input("you: ")
#         # print(f'you: {a}')
#         if a=='bye':
#             break
#         p=predict_class(a,model)
#         print(p)

#     except:
#         text="I Do Not Understand"
#         print(f"Alexa: {text}")


