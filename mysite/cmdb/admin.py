from django.contrib import admin

# Register your models here.
from cmdb.models import MovieInfo


class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ('userid', 'quote', 'comment')


admin.site.register(MovieInfo, MovieInfoAdmin) 

