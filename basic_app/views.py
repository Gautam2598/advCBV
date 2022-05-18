from email import contentmanager
from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,UpdateView,DeleteView)

from basic_app.forms import CompanyAddForm
from .models import *
from django.urls import reverse_lazy

class Indexview(TemplateView):
     template_name = 'basic_app/index.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['testdata'] = 'BASIC INJECTION'
#         return context

class CompanyListView(ListView):
    #there is an context object created automatically by the name of model and _list is added at the end
    #or we can create and name the context according to our choice
    context_object_name = 'company_list'
    model = Company

class CompanyCreateView(CreateView):
    form_class = CompanyAddForm
    model = Company

class CompanyUpdateView(UpdateView):
    fields = "__all__"
    model = Company

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy("index")

# class CompanyDetailView(DetailView):
#     context_object_name = 'company_detail'
#     model = Company
#     template_name = 'company_detail.html'

class DepartmentListView(ListView):
    model = Department

# class DepartmentDetailView(DetailView):
#     context_object_name = 'department_detail'
#     model = Department
#     template_name = 'department_detail.html'

class TechnologiesListView(ListView):
    model = Technologies

class ProjectListView(ListView):
    extra_context = {'compList':Company.objects.all()}
    model = Project 

class ProjectView(TemplateView):
    template_name = "basic_app/project_view.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['testdata'] = Project.objects.all()
        return context


class EmployeeListView(ListView):
    model = Employee