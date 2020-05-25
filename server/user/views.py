from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import UserSerializer
from .models import User, CustomUser
from rest_framework.authtoken.models import Token
import string, random


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 유저 전체
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    # 특정 유저 자세히
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()

        # URL Parameter로 유저 찾기
        user = get_object_or_404(queryset, username=pk)

        # 요청한 유저와 Parameter로 찾은 유저가 같으면, 또는 요청한 유저가 슈퍼 유저이면 유저 정보 전송, 아니면 권한 부족 전송
        if user == request.user or request.user.is_superuser:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({ "detail": "Authentication credentials were not provided." })

    # 유저 정보 수정
    def update(self, request, pk=None):
        queryset = User.objects.all()
        customqueryset = CustomUser.objects.all()

        # URL parameter로 유저 찾기
        user = get_object_or_404(queryset, username=pk)

        # 요청한 유저와 Parameter로 찾은 유저가 같으면, 또는 요청한 유저가 슈퍼 유저이면 유저 정보 수정, 아니면 권한 부족 전송
        if user == request.user or request.user.is_superuser:
            customuser = get_object_or_404(customqueryset, user_id=user.id)

            # Password 확인
            if check_password(request.data['password'], user.password) or request.user.is_superuser:
                if request.data.get('email'):
                    user.email = request.data['email']
                if request.data.get('new_password'):
                    user.password = make_password(request.data['new_password'])
                if request.data.get('hasSubscribed') == True or request.data.get('hasSubscribed') == False:
                    customuser.hasSubscribed = request.data['hasSubscribed']
                if request.data.get('topics'):
                    customuser.topics = request.data['topics']
                user.save()
                customuser.save()

                print(user.__dict__)
                return Response({ "id": user.id, "username": user.username, "email": user.email, "hasSubscribed": customuser.hasSubscribed, "topics": customuser.topics }, status=200)
            else:
                return Response({ "detail": "Incorrect password." }, status=401)
        else:
            return Response({ "detail": "Authentication credentials were not provided." }, status=401)

    # 유저 삭제
    def destroy(self, request, pk=None):
        queryset = User.objects.all()

        # URL parameter로 유저 찾기
        user = get_object_or_404(queryset, username=pk)

        # 요청한 유저와 Parameter로 찾은 유저가 같으면, 또는 요청한 유저가 슈퍼 유저이면 유저 정보 삭제, 아니면 권한 부족 전송
        if user == request.user or request.user.is_superuser:
            # Password 확인
            if check_password(request.data['password'], user.password) or request.user.is_superuser:
                user.is_active = False
                user.save()

        return Response(status=204)
    
    # 권한 설정
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class LostFindViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        
        # ID 찾기
        if pk == "find-id":
            user = get_object_or_404(queryset, email=request.data.get('email'))
            if user:
                return Response({"username": user.username})
            else:
                return Response({ "detail": "Not Found." }, status=404)
        
        # 비밀번호 찾기 (임시 비밀번호 만들기)
        elif pk == "find-password":
            user = get_object_or_404(queryset, username=request.data.get('username'))
            if user and user.email == request.data.get('email'):

                LENGTH = 10
                string_pool = string.ascii_lowercase
                randStr = ""
                for i in range(LENGTH):
                    randStr += random.choice(string_pool)

                user.password = make_password(randStr)
                user.save()

                # 임시로 Response로 전송함.
                return Response({"newpassword": randStr})

            else:
                return Response({"detail": "Not Found."}, status=404)
        
        # 알 수 없는 경우
        else:
            return Response({ "detail": "Bad Request." }, status=400)

    # 권한 설정
    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CheckSuperuserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def create(self, request):
        return Response({ "is_super": request.user.is_superuser })
