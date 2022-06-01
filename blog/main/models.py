from django.db import models

# Create your models here.
class Write(models.Model):
    title = models.CharField(max_length=50)	#글자 수가 제한된 텍스트 정의(짧은 문자열)
    contents = models.TextField()	#글자 수 제한이 없는 긴 텍스트 정의
    updated_at = models.DateTimeField(auto_now=True)	#날짜와 시간 정의