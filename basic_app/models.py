from django.db import models
from datetime import date
from datetime import datetime
from django.urls import reverse

class  Company(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("company_list")

class Department(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company,related_name='department',on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Technologies(models.Model):
    company = models.ManyToManyField(Company)
    name = models.CharField(max_length=36)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=64)
    employeeID = models.DateTimeField(auto_created=True,unique=True) #autoadd
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    attachments = models.FileField(upload_to='docs/')
    company = models.ForeignKey(Company,related_name='project',on_delete=models.DO_NOTHING)
    technologies = models.ManyToManyField(Technologies)
    startDate = models.DateField()
    endDate = models.DateField()
    employees = models.ManyToManyField(Employee)
    description = models.CharField(max_length=1000,default="Hello")

    def __str__(self):
        return self.name

