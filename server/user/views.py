from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer
from .models import User
from rest_framework.authtoken.models import Token


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
    
    # 권한 설정
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
