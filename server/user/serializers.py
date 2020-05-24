from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    hasSubscribed = serializers.BooleanField(source='customuser.hasSubscribed')
    topics = serializers.CharField(source='customuser.topics')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'hasSubscribed', 'topics')

    def create(self, validated_data):
        customUser_data = validated_data.pop('customuser', None)    # hasSubscribed를 customUser_data로 분리

        validated_data['password'] = make_password(validated_data.get('password'))  # 비밀번호를 해싱
        user = super(UserSerializer, self).create(validated_data)   # User 모델 기본 create 함수 호출
        create_auth_token(user) # user의 Token 생성

        self.update_or_create_customuser(user, customUser_data) # CustomUser 모델 생성 및 수정
        return user

    def update(self, instance, validated_data):
        customUser_data = validated_data.pop('customuser', None)    # hasSubscribed를 customUser_data로 분리
        self.update_or_create_customuser(instance, customUser_data) # CustomUser 모델 생성 및 수정

        validated_data['password'] = make_password(validated_data.get('password'))  # 비밀번호를 해싱
        return super(UserSerializer, self).update(instance, validated_data) # User 모델 기본 create 함수 호출

    def update_or_create_customuser(self, user, customUser_data):
        # This always creates a Profile if the User is missing one;
        # change the logic here if that's not right for your app
        CustomUser.objects.update_or_create(user=user, defaults=customUser_data)


def create_auth_token(user):
    # Token 생성 코드 : 새로운 User에 인증을 위한 토큰 생성
    Token.objects.get_or_create(user=user)