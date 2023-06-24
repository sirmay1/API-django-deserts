from django.shortcuts import render
from .models import Desert
from .serializers import DesertSerializer
from rest_framework import viewsets


class DesertView(viewsets.ModelViewSet):
    queryset = Desert.objects.all()
    serializer_class = DesertSerializer
