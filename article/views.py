from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from article.models import Article, Commentary


def index(request):
    return HttpResponseRedirect('/articles/all/')


def articles(request):
    return render_to_response('index.html',
                              {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html',
                              {'article': Article.objects.get(id=article_id),
                               'commentaries': Commentary.objects.filter(commentary_article_id=article_id)})
