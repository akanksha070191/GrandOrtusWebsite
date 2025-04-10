from rest_framework import serializers
from .models import JobProfile

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProfile
        fields = '__all__'