from django.contrib import admin
from .models import artist, duration, title, albums, date_added

@admin.register(artist)
class artistAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "created_at", "updated_at")
    search_fields = ("FirstName", "LastName", "Email",)

@admin.register(duration)
class durationAdmin(admin.ModelAdmin):
    list_display = ("durationName", "artistID", "created_at", "updated_at")
    search_fields = ("durationName", "artistID__FirstName", "artistID__LastName", "artistID__Email")

@admin.register(title)
class titleAdmin(admin. ModelAdmin):
    list_display = ("SongName", "Artist", "Duration","created_at","updated_at")
    search_fields = ("SongName", "Artist", "Duration")

@admin.register(albums)
class albumsAdmin(admin. ModelAdmin):
    list_display = ("titleID", "durationID","created_at","updated_at")
    search_fields = ("titleID__FirstName", "titleID__LastName", "durationID__durationName")

class date_addedAdmin(admin.ModelAdmin):
    list_display = ('Song_Added', 'durationID')
    search_fields = ("Song_Added", "durationID__durationName")

