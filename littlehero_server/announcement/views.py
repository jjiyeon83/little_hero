import json
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from .serializers import *
from .models import Post
import django_filters
from .filters import *
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.http import require_POST
from django.http import HttpResponse

# Create your views here.

# view when you click the title of post.
# you need regist_no and site_domain in query 
class PostViewDetail(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostDetailFilter


# pagination
class PostPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'

# query handling of notice board
class PostView(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostFilter
    pagination_class = PostPagination
    search_fields = ['title']


# update likes
def post_like(request, pk):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    if post.likes_post.filter(id=user.id).exists() :
        post.likes_post.remove(user)
        message = '좋아요 취소'
    else :
        video.likes_post.add(user)
        message = '좋아요'

    context = {'likes_count' : post.count_liked_user(), 'message' : message}
    return HttpResponse(json.dumps(context), context_type = "application/json")



# get dropdown
class DropDownView(generics.ListAPIView):
    queryset = Dropdown.objects.all()
    serializer_class = DropDownSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = DropDownFilter
