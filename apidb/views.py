#from django.shortcuts import render

# Create your views here.
#from django.views.generic import ListAPIView


from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer
class DBAPIView(generics.ListAPIView):
    queryset = Actor.objects.filter(last_name = "Guiness")
    serializer_class = ActorSerializer