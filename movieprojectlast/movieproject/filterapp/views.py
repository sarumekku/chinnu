# import movie
# from django.shortcuts import render
#
# from filterapp.models import MovieFilter
#
#
# # Create your views here.
# def movie_list(request):
#     filter = MovieFilter(request.GET, queryset=movie.object.all())
#     return render(request, 'filter.html', {'filter':'filter'})