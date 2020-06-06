from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
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


class PostCountViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()

        # URL Parameter로 유저 찾기
        post = get_object_or_404(queryset, id=pk)

        if post != None:
            post.count += 1
            post.save()

        return Response({}, status=200)

class PostSWCountViewSet(viewsets.ModelViewSet):
    serializer_class = PostSWSerializer
    queryset = PostSW.objects.all()

    def list(self, request):
        queryset = PostSW.objects.all()
        serializer = PostSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = PostSW.objects.all()

        # URL Parameter로 유저 찾기
        post_sw = get_object_or_404(queryset, id=pk)

        if post_sw != None:
            post_sw.count += 1
            post_sw.save()

        return Response({}, status=200)
