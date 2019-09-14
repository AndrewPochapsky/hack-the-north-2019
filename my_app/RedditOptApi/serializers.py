from rest_framework import serializers
from .models import InputBox, Output   #import model

# Create a class
class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputBox
        fields = '__all__'

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = '__all__'
