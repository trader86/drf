from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

class ArticleList(ListView):
    def get_queryset(self):
        return Article.objects.filter(status=True)