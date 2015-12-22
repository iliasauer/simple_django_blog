from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf

from article.forms import CommentaryForm
from article.models import Article, Commentary


def index(request):
    return redirect('/articles/all/')


def articles(request):
    return render_to_response('articles.html',
                              {'articles': Article.objects.all(),
                               'username': auth.get_user(request).username})


def article(request, article_id=1):
    commentary_form = CommentaryForm()
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['commentaries'] = Commentary.objects.filter(commentary_article_id=article_id)
    args['form'] = commentary_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):
    try:
        article_obj = Article.objects.get(id=article_id)
        article_obj.article_likes += 1
        article_obj.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def addcommentary(request, article_id):
    if request.POST:
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.commentary_article = Article.objects.get(id=article_id)
            form.save()
    return redirect('/articles/get/%s/' % article_id)


