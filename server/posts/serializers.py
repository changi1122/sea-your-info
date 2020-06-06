from rest_framework import serializers
from .models import Post, PostSW

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # 모델 설정
        fields = ('id', 'title', 'date', 'url', 'type', 'isSent', 'count') # 필드 설정

class PostSWSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSW # 모델 설정
        fields = ('id', 'title', 'date', 'url', 'type', 'isSent', 'count') # 필드 설정
