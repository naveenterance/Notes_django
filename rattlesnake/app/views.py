from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from .models import Notes
import re
from django.db import connection
from django.views.generic.base import TemplateView

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

class MyView(TemplateView):
    template_name = "../templates/app/log.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        insert='INSERT'
        delete='+'

        f = open("debug.log", "r")

        line2=""
        p1=""

        line_number = 0
        list_of_results = []

        # Open the file in read only mode
        with open("debug.log", "r") as read_obj:
            # Read all lines in the file one by one
            for line in read_obj:
                # For each line, check if line contains the string
                line_number += 1
                if insert in line:

                    start = line.find("@@") + len("@@")

                    end = line.find("$$")

                    line_time = line[start:end]

                    line_time =" <div class='timeline' ><a  class='timeline-content' style=' color: rgb(1, 194, 163); border-color:rgb(1, 194, 163) ;'><div class='timeline-year' style=' color: rgb(1, 194, 163);' >"+line_time



                    

                    start = line.find("&&") + len("&&")

                    end = line.find("@@")

                    line_date = line[start:end]

                    line_date ="</div><div class='timeline-icon'><i class='far fa-plus-square' style='color:rgb(1, 194, 163);'></i></div><h3 class='title'>Added </h3><h5>"+line_date


                    start = line.find("(\'") + len("(\'")

                    end = line.find("\',")

                    line1 = line[start:end]

                    line1= "</h5><p class='description'><h3>'" + line1 +"'</h3> </p></a></div>"

                  


                    line2 = line2 +line_time+line_date+ line1
                  


                                    
                if delete in line:

                    start = line.find("@@") + len("@@")

                    end = line.find("$$")

                    line_time = line[start:end]

                    line_time =" <div class='timeline' ><a  class='timeline-content' style=' color: rgb(255, 45, 90); border-color: rgb(255, 45, 90);'><div class='timeline-year' style=' color: rgb(255, 45, 90);'>"+line_time



                    

                    start = line.find("&&") + len("&&")

                    end = line.find("@@")

                    line_date = line[start:end]

                    line_date ="</div><div class='timeline-icon'><i class='far fa-trash-alt' style='color:rgb(255, 45, 90);'></i></div><h3 class='title'>Deleted </h3><h5>"+line_date


                    start = line.find("+") + len("+")

                    end = line.find("++")

                    line1 = line[start:end]

                    line1= "</h5><p class='description'><h3>" + line1 +" </h3></p></a></div>"

                  


                    line2 = line2 +line_time+line_date+ line1
                  


        context['line']=line2               
        
        return context
        #return HttpResponse("<h5>%s<h5>"%line2)
               
