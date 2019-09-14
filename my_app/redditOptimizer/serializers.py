from rest_framework import serializers
from .models import InputBox

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = InputBox
