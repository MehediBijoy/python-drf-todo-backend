from django.db.models import fields
from rest_framework import serializers
from .models import todoModel

class todoSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user')
    class Meta:
        model = todoModel
        fields = ['user', 'username', 'task', 'status']
        read_only_fields = ['username']
        extra_kwargs = {'user': {'write_only': True}}
