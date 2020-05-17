from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hasSubscribed = models.BooleanField(default=False)      # 이메일을 구독했는지 여부 : true면 이메일 전송
    topics = models.TextField(default="")                   # 관심 있는 분야 (리스트를 문자열로 저장)
