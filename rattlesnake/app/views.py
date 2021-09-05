from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from .models import Notes

# Create your views here.

class NotesList(ListView):
    model = Notes

class NotesDetail(DetailView):
    model = Notes

class NotesCreate(CreateView):
    model = Notes
    # Field must be same as the model attribute
    fields = ['title', 'content', 'urgency']
    success_url = reverse_lazy('notes_list')

class NotesUpdate(UpdateView):
    model = Notes
    # Field must be same as the model attribute
    fields = ['title', 'content', 'urgency']
    success_url = reverse_lazy('notes_list')

class NotesDelete(DeleteView):
    model = Notes
    success_url = reverse_lazy('notes_list')

class MyView(View):

    def get(self, request, *args, **kwargs):
        insert='INSERT'
        delete='DELETE'

        f = open("debug.log", "r")


        line_number = 0
        list_of_results = []

        # Open the file in read only mode
        with open("debug.log", "r") as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                line_number += 1
                if insert in line:
                # If yes, then add the line number & line as a tuple in the list
                    list_of_results.append(("<h1>Added<h1>",line.rstrip()))
                if delete in line:
                    list_of_results.append(("<h1>Deleted<h1>",line.rstrip()))
            # Return list of tuples containing line numbers and lines where string is found
        return HttpResponse("<h5>%s<h5>"%list_of_results)
               