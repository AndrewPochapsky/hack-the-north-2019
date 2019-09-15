from django.shortcuts import render
from rest_framework import generics

from .models import InputBox, OutputBox
from .serializers import InputSerializer, OutputSerializer

from rest_framework import viewsets

#Create your views here.
class ListInput(generics.ListAPIView):
    queryset = InputBox.objects.all()
    serializer_class = InputSerializer

class ListCreateInput(generics.CreateAPIView):
    queryset = InputBox.objects.all()
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

def formSubmission():
    #delete entries from OutputBox
    OutputBox.objects.all().delete()
    #generate the outputBox
