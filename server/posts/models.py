from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)        # 제목 : 최대 100자
    date = models.DateTimeField()                   # 게시일
    url = models.TextField()                        # URL
    type = models.TextField()                       # 유형 : 필터링에 사용, 리스트를 문자열로 바꿔 저장

    def __str__(self):
        return self.title

