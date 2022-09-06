from dataclasses import field
from rest_framework import serializers
from .models import student_info

class StudentInfoSerelizers(serializers.ModelSerializer):
    class Meta:
        model = student_info
        fields = '__all__'

    