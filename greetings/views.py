# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Greeting


# https://cloud.google.com/appengine/docs/python/datastore/datamodeling
# DB datastore model 적용

# https://cloud.google.com/appengine/docs/python/ndb
# NDB 적용 (entity 개념을 적용해서 'N'DB 인가?;)
# NDB 의 장점은 위 링크의 첫번째 단락을 읽어보면 된다.

# DB => NDB cheetsheet
# https://docs.google.com/document/d/1AefylbadN456_Z7BZOpZEXDq8cR8LYu7QgI7bt5V0Iw/edit?ndplr=1&pli=1



def all_greetings(request):
    greetings = Greeting.query(Greeting.name == 'eee')  # objects.all => all => query
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
