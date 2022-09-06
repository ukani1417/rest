

from django.shortcuts import render
from .models import student_info
from .serializers import StudentInfoSerelizers

from rest_framework import generics
from rest_framework import mixins


class StudentGenericView(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin
                         ):
    serializer_class = StudentInfoSerelizers
    queryset = student_info.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request,id = None):
        return self.create(request)

    def put(self, request, id = None):
        return self.update(request)

    def delete(self, request, id=None):
        return self.destroy(request,id)
