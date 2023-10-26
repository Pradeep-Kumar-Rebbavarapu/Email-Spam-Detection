from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
BASE_DIR = settings.BASE_DIR
import pickle
import os

model = pickle.load(open(os.path.join(BASE_DIR,'model.pkl'),'rb'))

def index(request):
    return render(request,'index.html')

def qn2(request):
    if request.method=="POST":
        text = request.POST.get('message')
        message = [text]
        print(message)
        prediction = model.predict(message)
        if prediction==1:
            spam = "This is a spam message"
        else:
            spam = "This is not a spam message"
        return render(request,'qn2.html',{'prediction_text':spam})
    return render(request,'qn2.html')

    