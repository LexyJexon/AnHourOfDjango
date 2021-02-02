from django.shortcuts import render
from articles.models import Article


def index(request):
    articles_list = Article.objects.order_by('id')
    return render(request, 'mainpage.html', {'articles_list': articles_list})
