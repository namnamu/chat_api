from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200) # 문자 필드
#     pub_date = models.DateTimeField("date published") # 날짜와 시간 필드


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)# 1개의 choice가 1개의 Question에 관계된다.
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Question_Answer(models.Model):
    ID = models.CharField(max_length=200) 
    user_key = models.CharField(max_length=200)
    Answer = models.CharField(max_length=200)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    #is_accepted
    view_count = models.IntegerField(default=0)
    Keywords = models.CharField(max_length=200)
    Date = models.DateTimeField("date published") 
    Links = models.CharField(max_length=200) 