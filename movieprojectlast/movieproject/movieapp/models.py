from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Movie(models.Model):
    choices = [
        ("Horror", "Horror"),
        ("Thriller", "Thriller"),
        ("Action", "Action"),
        ("Romance", "Romance"),
        ("Comedy", "Comedy"),
        ("Animated", "Animated"),
    ]
    title = models.CharField(max_length=250)
    description = models.TextField()
    poster = models.ImageField(upload_to="gallery")
    date = models.DateField()
    actors = models.CharField(max_length=200)
    category = models.CharField(max_length=200,choices=choices,null=True)
    # trailer_link = models.URLField()
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering=('title',)
        verbose_name='Movie'
        verbose_name_plural='Movies'

    def __str__(self):
        return self.title


# class Review(models.Model):
#     rating = models.IntegerField()
#     comment = models.TextField()
#
#
#     class Meta:
#         ordering=('rating',)
#         verbose_name='Review'
#         verbose_name_plural='Reviews'
#
#     def __str__(self):
#         return self.rating





