# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Greeting


# https://cloud.google.com/appengine/docs/python/datastore/datamodeling
# DB datastore model 적용


def all_greetings(request):
    greetings = Greeting.all()  # objects.all => all
    res = "<h3> GREETINGS </h3>"

    # 인사말 라인단위 출력
    for i in greetings:
        res += unicode(i)
        res += "<br>"

    # 새 인사말 페이지 링크
    res += "<h3><a href='/greetings/new'>new greeting</a></h3>"

    return HttpResponse(res)


def new_greeting(request):

    # 새 인사말 페이지
    if request.method == "GET":
        res = """<form action="/greetings/new/"
                       method="post">
        message: <input type="text" name="message"><br>
        name: <input type="text" name="name"><br>
        <input type="submit" name="greet">
        </form>"""
        return HttpResponse(res)

    # 새 인사말 등록 및 전체 페이지로 이동
    elif request.method == "POST":

        message = request.POST["message"]
        name = request.POST["name"]

        greeting = Greeting(message=message, name=name)

        greeting.put()  # save => put
        return redirect('/greetings')  # WTF! new greeting delayed!
