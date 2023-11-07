# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Question_Answer

def index(request):
    latest_question_list = Question_Answer.objects.order_by("-ID")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context,request))# 화면상에 보인다.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)