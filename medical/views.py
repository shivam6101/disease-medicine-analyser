# import wikipedia
import pytesseract as tess
import numpy as np
tess.pytesseract.tesseract_cmd=r'C:\Users\Shivam\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image

import requests
from django.shortcuts import render
from tensorflow.keras.models import load_model
model=load_model('Medicin_Model.h5')
diseas_model=load_model('Diseas_Model.h5')
from medicine_analyse import predict_information,predict_usage
from diseas_analyser import predict_precaution,predict_diseas,predict_medicin

def home(request):
    return render(request,"home.html")

def diseas(request):
    return render(request,'diseas.html')
def diseas_analyser(request):
    if request.method=='POST':
        symptom=request.POST.get("symptoms")
        if(symptom==""):
            return render(request,'diseas.html')
        precaution=predict_precaution(symptom,diseas_model)
        medicine=predict_medicin(symptom,diseas_model)
        diseas_name=predict_diseas(symptom,diseas_model)
    context={"precaution":precaution,"medicine":medicine,"diseas_name":diseas_name}
    return render(request,'diseas.html',context)



def index(request):
    return render(request,'index.html')
def create(request):
    if request.method=='POST':
        salt=request.POST.get("name")
        if(salt==""):
            return render(request,'index.html')
        # info=wikipedia.summary(salt,1)
        data=predict_information(salt,model)
        info=predict_usage(salt,model)
    context={"data":data,"info":info}
    return render(request,'index.html',context)

def image_ocr(request):
    if request.method=='POST':
        img=request.POST.get("image")
        if(img==""):
            return render(request,'index.html')
        text=(r"C:\Users\Shivam\OneDrive\Desktop\tcs_project\easyocr")
        img=Image.open(text+f"\{img}")
        salt=tess.image_to_string(img)
        data=predict_information(salt,model)
        info=predict_usage(salt,model)
    context={"data":data,"info":info}
    return render(request,'index.html',context)

def camimg(request):
    if request.method=='POST':
        salt=request.POST.get("result")
        if(salt==""):
            return render(request,'index.html')
        data=predict_information(salt,model)
        info=predict_usage(salt,model)
    context={"data":data,"info":info}
    return render(request,'index.html',context)

 
    