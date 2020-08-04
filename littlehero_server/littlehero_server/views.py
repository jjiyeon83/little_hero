import django_filters
from .filters import  SearchFilter, ViewFilter
from rest_framework import filters
from .models import Post
from .serializers import SearchSerializer, ViewSerializer
from rest_framework import generics

class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ViewSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ViewFilter

class SearchView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = SearchFilter
