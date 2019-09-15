from rest_framework import serializers
from .models import InputBox, OutputBox

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = InputBox

class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = OutputBox
