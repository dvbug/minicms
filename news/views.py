# coding: utf-8
"""
    news.views
    ~~~~~~~~~~

    :copyright: (c) 2016 by Vito.
    :license: GNU, see LICENSE for more details.
"""

from django.shortcuts import render, redirect
# from django.core.urlresolvers import reverse
# from django.http import HttpResponse
from .models import Column, Article


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request, 'news/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)  # permanent 永久性跳转 301
    return render(request, 'news/article.html', {'article': article})
