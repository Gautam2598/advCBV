"""cbviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Indexview.as_view(),name='index'),
    path('company_list', views.CompanyListView.as_view(),name='company_list'),
    path('companyCreate', views.CompanyCreateView.as_view(),name='companyCreate'),
    path('companyUpdate/<int:pk>', views.CompanyUpdateView.as_view(),name='companyUpdate'),
    path('companyDelete/<int:pk>', views.CompanyDeleteView.as_view(),name='companyDelete'),
    path('department_list', views.DepartmentListView.as_view(),name='department_list'),
    path('project_list', views.ProjectListView.as_view(),name='project_list'),
    path('project_add/<int:pk>', views.ProjectView.as_view(),name='project_add'),
    path('technologies_list', views.TechnologiesListView.as_view(),name='technologies_list'),
    path('employee_list', views.EmployeeListView.as_view(),name='employee_list'),
    
]
