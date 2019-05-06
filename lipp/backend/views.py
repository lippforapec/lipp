from django.shortcuts import render
from rest_framework import viewsets
from backend.models import Article
from backend.serializers import ArticleSerializer
# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API for Articles
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

