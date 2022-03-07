#Django Girls tutorial says to create this 2nd urls.py file

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.albums_list, name='albums_list'),
    path('albums/add_album/', views.add_album, name='add_album'),
    # path('albums/<int:pk>/edit/', views.edit_album, name='edit_album')
]


# <!-- <a class="btn btn-secondary" href="{% url 'edit_album' pk=album.pk %}"> -->
#             <!-- <a href="{% url 'edit_album' pk=album.pk %}">Edit Album</a><br>    
#             <a class="red" href="{% url 'delete_album' pk=album.pk %}">Delete Album</a> -->