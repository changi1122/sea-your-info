from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, PostSWSerializer
from .models import Post, PostSW

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostSWViewSet(viewsets.ModelViewSet):
    queryset = PostSW.objects.all()
    serializer_class = PostSWSerializer
