from django_filters import FilterSet, NumberFilter, CharFilter, BooleanFilter
from .models import Post

class SearchFilter(Filterset):
    registNo = NumberFilter(name='registNo')
    siteDomain = NumberFilter(name='siteDomain')

    class Meta :
        model = Post
        fields = ['registNo', 'siteDomain']

class ViewFilter(Filterset):
    title = CharFilter(name='title')
    addressCity = CharFilter(name='address_city')
    addressGu = CharFilter(name='address_gu')
    recruitStatus = BooleanFilter(name='recruit_status')
    adultStatus = BooleanFilter(name='adult_status')

    class Meta :
        model = Post
        fields = ['title', 'addressCity', 'addressGu', 'recruitStatus', 'adultstatus']
