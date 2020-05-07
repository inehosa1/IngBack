from django.shortcuts import render
from management.models import Example
from management.serializers import ExampleSerializer
from rest_framework import viewsets


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer