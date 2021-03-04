from django.shortcuts import render
from .serializers import MarketListSerializers
from .models import MarketList
from rest_framework import viewsets

# Create your views here.
class MarketListView(viewsets.ModelViewSet):
    serializer_class = MarketListSerializers
    queryset = MarketList.objects.all()