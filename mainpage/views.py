from django.shortcuts import render
from articles.models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'base.html', {'latest_articles_list': latest_articles_list})
