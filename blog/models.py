from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    body = RichTextUploadingField()
    created_time = models.DateTimeField('发布时间')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_date <=now




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
