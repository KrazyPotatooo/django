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
class titleAdmin(admin.ModelAdmin):
    list_display = ("titleID", "FirstName", "LastName", "get_artist")  # Replace 'get_artist' with the correct method
    # Other admin configurations

    def get_artist(self, obj):
        return obj.artist  # Replace 'artist' with the actual field name
    get_artist.short_description = 'Artist'  # Display name for the column

@admin.register(albums)
class albumsAdmin(admin.ModelAdmin):
    list_display = ("artist", "song", "created_at", "updated_at")  # Assuming field names are 'artist' and 'song'
    search_fields = ("artist__FirstName", "song__song_name")  # Assuming 'song_name' is a field in the 'song' model

@admin.register(date_added)
class date_addedAdmin(admin.ModelAdmin):
    list_display = ("date_addedName", "Deadline", "durationID", "created_at", "updated_at")
    search_fields = ("date_addedName", "durationID__durationName")
