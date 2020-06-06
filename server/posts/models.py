from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)        # 제목 : 최대 100자
    date = models.DateTimeField()                   # 게시일
    url = models.TextField()                        # URL
    type = models.TextField()                       # 유형 : 필터링에 사용, 리스트를 문자열로 바꿔 저장
    isSent = models.BooleanField(default=False)     # 이메일 전송 여부 : true면 이미 전송됨
    count = models.IntegerField(default=0)          # 클릭 수 카운터

    def __str__(self):
        return self.title

class PostSW(models.Model):
    title = models.CharField(max_length=100)        # 제목 : 최대 100자
    date = models.DateTimeField()                   # 게시일
    url = models.TextField()                        # URL
    type = models.TextField()                       # 유형 : 필터링에 사용, 리스트를 문자열로 바꿔 저장
    isSent = models.BooleanField(default=False)     # 이메일 전송 여부 : true면 이미 전송됨
    count = models.IntegerField(default=0)          # 클릭 수 카운터

    def __str__(self):
        return self.title

