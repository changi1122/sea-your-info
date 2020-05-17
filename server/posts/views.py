from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import *
from .serializers import PostSerializer, PostSWSerializer
from .models import Post, PostSW


class PostViewSet(viewsets.ModelViewSet):
    # Admin User가 아니면 읽기만 허용, Admin User이면 읽기와 쓰기 모두 허용
    permission_classes = (IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly,)

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostSWViewSet(viewsets.ModelViewSet):
    # Admin User가 아니면 읽기만 허용, Admin User이면 읽기와 쓰기 모두 허용
    permission_classes = (IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly,)

    queryset = PostSW.objects.all()
    serializer_class = PostSWSerializer
