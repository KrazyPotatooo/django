from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from record.models import artist, duration, title, albums, date_added
from record.forms import artistForm,durationForm,titleForm,date_addedForm,albumsForm
from django.urls import reverse_lazy





class HomePageView(ListView):
    model = title
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context
class artistListView(ListView):
    model = artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'
    paginate_by = 5

    def get_queryset(self):
        return artist.objects.all()
    
class artistCreateView(CreateView):
    model = artist
    form_class = artistForm
    template_name = 'artist_add.html'
    success_url = reverse_lazy('artist-list')
    
class artistUpdateView(UpdateView):
    model = artist
    form_class = artistForm
    template_name = 'artist_edit.html'
    success_url = reverse_lazy('artist-list')
    
class artistDeleteView(DeleteView):
    model = artist
    template_name = 'artist_del.html'
    success_url = reverse_lazy('artist-list')  

class durationListView(ListView):
    model = duration
    template_name = 'duration_list.html'
    context_object_name = 'durations'
    paginate_by = 5

    def get_queryset(self):
        return duration.objects.all()
    
class durationCreateView(CreateView):
    model = duration
    form_class = durationForm
    template_name = 'duration_add.html'
    success_url = reverse_lazy('duration-list')
    
class durationUpdateView(UpdateView):
    model = duration
    form_class = durationForm
    template_name = 'duration_edit.html'
    success_url = reverse_lazy('duration-list')
    
class durationDeleteView(DeleteView):
    model = duration
    template_name = 'duration_del.html'
    success_url = reverse_lazy('duration-list')  

class titleListView(ListView):
    model = title
    template_name = 'title_list.html'
    context_object_name = 'titles'
    paginate_by = 5

    def get_queryset(self):
        return title.objects.all()

class titleCreateView(CreateView):
    model = title
    form_class = titleForm
    template_name = 'title_add.html'
    success_url = reverse_lazy('title-list')
    
class titleUpdateView(UpdateView):
    model = title
    form_class = titleForm
    template_name = 'title_edit.html'
    success_url = reverse_lazy('title-list')
    
class titleDeleteView(DeleteView):
    model = title
    template_name = 'title_del.html'
    success_url = reverse_lazy('title-list')  
    
class albumsListView(ListView):
    model = albums
    template_name = 'albums_list.html'
    context_object_name = 'albumss'
    paginate_by = 5

    def get_queryset(self):
        return albums.objects.all()
    
class albumsCreateView(CreateView):
    model = albums
    form_class = albumsForm
    template_name = 'albums_add.html'
    success_url = reverse_lazy('albums-list')
    
class albumsUpdateView(UpdateView):
    model = albums
    form_class = albumsForm
    template_name = 'albums_edit.html'
    success_url = reverse_lazy('albums-list')
    
class albumsDeleteView(DeleteView):
    model = albums
    template_name = 'albums_del.html'
    success_url = reverse_lazy('albums-list') 

class date_addedListView(ListView):
    model = date_added
    template_name = 'date_added_list.html'
    context_object_name = 'date_added'
    paginate_by = 5

    def get_queryset(self):
        return date_added.objects.all()
    
class date_addedCreateView(CreateView):
    model = date_added
    form_class = date_addedForm
    template_name = 'date_added_add.html'
    success_url = reverse_lazy('date_added-list')
    
class date_addedUpdateView(UpdateView):
    model = date_added
    form_class = date_addedForm
    template_name = 'date_added_add.html'
    success_url = reverse_lazy('date_added-list')
    
class date_addedDeleteView(DeleteView):
    model = date_added
    template_name = 'date_added_del.html'
    success_url = reverse_lazy('date_added-list') 
