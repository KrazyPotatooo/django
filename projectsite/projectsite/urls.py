from django.contrib import admin
from django.urls import path
from record.views import (
    HomePageView, artistListView, artistCreateView, artistDeleteView, artistUpdateView,
    durationListView, durationCreateView, durationDeleteView, durationUpdateView,
    titleListView, titleCreateView, titleDeleteView, titleUpdateView,
    albumsListView, albumsCreateView, albumsDeleteView, albumsUpdateView,
    date_addedListView, date_addedCreateView, date_addedDeleteView, date_addedUpdateView,
    albumsUpdateView,  # Importing specifically for use in the URLs
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('artists/', artistListView.as_view(), name='artist-list'),
    path('artists/add/', artistCreateView.as_view(), name='artist-add'),
    path('artists/<int:pk>/', artistUpdateView.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', artistDeleteView.as_view(), name='artist-delete'),
    path('durations/', durationListView.as_view(), name='duration-list'),
    path('durations/add/', durationCreateView.as_view(), name='duration-add'),
    path('durations/<int:pk>/', durationUpdateView.as_view(), name='duration-update'),
    path('durations/<int:pk>/delete/', durationDeleteView.as_view(), name='duration-delete'),
    path('titles/', titleListView.as_view(), name='title-list'),
    path('titles/add/', titleCreateView.as_view(), name='title-add'),
    path('titles/<int:pk>/', titleUpdateView.as_view(), name='title-update'),
    path('titles/<int:pk>/delete/', titleDeleteView.as_view(), name='title-delete'),
    path('albums/', albumsListView.as_view(), name='albums-list'),
    path('albums/add/', albumsCreateView.as_view(), name='albums-add'),
    path('albums/<int:pk>/', albumsUpdateView.as_view(), name='albums-update'),
    path('albums/<int:pk>/delete/', albumsDeleteView.as_view(), name='albums-delete'),
    path('date_addeds/', date_addedListView.as_view(), name='date_added-list'),
    path('date_addeds/add/', date_addedCreateView.as_view(), name='date_added-add'),
    path('date_addeds/<int:pk>/', date_addedUpdateView.as_view(), name='date_added-update'),
    path('date_addeds/<int:pk>/delete/', date_addedDeleteView.as_view(), name='date_added-delete'),
    path('albums/update/', albumsUpdateView.as_view(), name='albums-update'),  # Use the imported view directly
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
