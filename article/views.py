from django.http import HttpResponse
from django.shortcuts import render
from article.models import Article


def all_articles(request):
    articles = Article.objects.all().values()
    return render(request, 'article_list.html', {
        'articles': articles
    })


def article_by_id(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'article_detail.html', {
        'article': article
    })
