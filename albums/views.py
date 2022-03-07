from django.shortcuts import render, redirect, get_object_or_404
#from django.utils import timezone
from .models import Album
from .forms import AlbumForm

# Create your views here.

def albums_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums_list.html', {"albums": albums})

#"title": title, "artist": artist, "text": text, "created_date": created_date ??

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='albums_list')   
    return render(request, "albums/add_album.html", {"form": form})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm
    return render(request, "albums/album_detail.html", {"album": album, "form": form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='albums_list')
        
    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })
    
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='albums_list')

    return render(request, "albums/delete_album.html",
                {"album": album})