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
    user_key = models.CharField(max_length=200, null=True)
    Question = models.CharField(max_length=200,default='질문') # 질문(필수)
    Answer = models.CharField(max_length=200,default='답변') # 답변(필수)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    is_accepted=models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    Keywords = models.CharField(max_length=200, null=True)
    Date = models.DateTimeField(auto_now_add=True)
    Links = models.CharField(max_length=200, null=True)