import json

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, ArticleModelsSerializer
from webapp.models import Article


# Create your views here.


class ArticleView(APIView):
    serializer_class = ArticleModelsSerializer

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        articles_data = self.serializer_class(articles, many=True).data
        return Response(articles_data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = self.serializer_class(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailView(APIView):
    serializer_class = ArticleModelsSerializer

    def get(self, request, *args, pk, **kwargs):
        articles = get_object_or_404(Article, pk=pk)
        articles_data = self.serializer_class(articles).data
        return Response(articles_data)
