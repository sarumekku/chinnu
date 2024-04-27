import django_filters

from movieapp.models import Movie


class MovieFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(lookup_expr='icontains',field_name='category')
    class Meta:
        model = Movie
        fields = ['title','category']