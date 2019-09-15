from django.shortcuts import render
from rest_framework import generics

from .models import InputBox, OutputBox
from .serializers import InputSerializer, OutputSerializer

from rest_framework import viewsets

import importlib
#nlp_predict = importlib.import_module('my_app.nlp.main')
#import my_app.nlp.main as nlp_predict
from . import nlp

def formSubmission(queryset):
    #delete entries from OutputBox
    OutputBox.objects.all().delete()
    #generate the outputBox

    q = queryset[::1]
    if(len(q)==1):
        top_5 = nlp.main.get_subreddits(q[0].title, q[0].body)
        for element in top_5:
            ListCreateOutput({subred:element})


#Create your views here.
class ListInput(generics.ListAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer

class ListCreateInput(generics.CreateAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer
    formSubmission(queryset)

class ListDeleteInput(generics.DestroyAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer

class ListOutput(generics.ListAPIView):
    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer

class ListCreateOutput(generics.CreateAPIView):
    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer
    InputBox.objects.all().delete()

class ListDeleteOutput(generics.DestroyAPIView):
    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer
