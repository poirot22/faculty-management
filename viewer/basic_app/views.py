from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models

from django.urls import reverse_lazy
# Create your views here.

class FacultyListView(ListView):
    model=models.Faculty

class FacultyDetailView(DetailView):
    model=models.Faculty
    template_name='basic_app/faculty.html'

class FacultyCreateView(CreateView):
    fields=('name','age','designation','gender','dob','faculty_id','blood_group','aadhar_no',
    'pan_no','mobile','email','state','district','pin','permanentAddressSameAsCurrentAddress',
    'qualification','college','university','percentage','award','year_award','org_award',
    'journal_name','journal_vol','issn_no','publisher','year_of_publication','article_title',
    'project_title','duration','cost_of_project','funding_agency','start_date','end_date'
    )
    model=models.Faculty

class FacultyUpdateView(UpdateView):
    fields=('name','age','designation','gender','dob','faculty_id','blood_group','aadhar_no',
    'pan_no','mobile','email','state','district','pin','permanentAddressSameAsCurrentAddress',
    'qualification','college','university','percentage','award','year_award','org_award',
    'journal_name','journal_vol','issn_no','publisher','year_of_publication','article_title',
    'project_title','duration','cost_of_project','funding_agency','start_date','end_date'
    )
    model=models.Faculty

class FacultyDeleteView(DeleteView):
    model=models.Faculty
    success_url=reverse_lazy('basic_app:list')



def searchbar(request):
    if request.method=='GET':
        search=request.GET.get('search')
        facs=models.Faculty.objects.all().filter(faculty_id=search)

        return render(request,'basic_app/searchbar.html',{'facs':facs})
