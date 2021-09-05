from django.urls import path
from . import views
from app.views import MyView


urlpatterns = [
    path('', views.NotesList.as_view(), name='notes_list'),
    path('view/<int:pk>', views.NotesDetail.as_view(), name='notes_detail'),
    path('new', views.NotesCreate.as_view(), name='notes_new'),
    path('edit/<int:pk>', views.NotesUpdate.as_view(), name='notes_edit'),
    path('delete/<int:pk>', views.NotesDelete.as_view(), name='notes_delete'),

    path('log', MyView.as_view(), name='log'),

]
