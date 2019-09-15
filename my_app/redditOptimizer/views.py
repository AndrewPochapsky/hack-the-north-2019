from django.shortcuts import render
from rest_framework import generics

from .models import InputBox, OutputBox
from .serializers import InputSerializer, OutputSerializer

from rest_framework import viewsets

import importlib
#nlp_predict = importlib.import_module('my_app.nlp.main')
#import my_app.nlp.main as nlp_predict
from . import main

def formSubmission(queryset):
    OutputBox.objects.all().delete()
    q=queryset.get()
    top_5 = main.get_subreddits(q.title, q.description)
    for element in top_5:
        OutputBox(subred=element,link='').save()
    InputBox.objects.all().delete()


#Create your views here.
class ListInput(generics.ListAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer

class ListCreateInput(generics.CreateAPIView):

    queryset = InputBox.objects.all()
    formSubmission(queryset)
    serializer_class = InputSerializer



class ListDeleteInput(generics.DestroyAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer

class ListOutput(generics.ListAPIView):
    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer

class ListCreateOutput(generics.CreateAPIView):

    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer


class ListDeleteOutput(generics.DestroyAPIView):
    queryset = OutputBox.objects.all()
    serializer_class = OutputSerializer
