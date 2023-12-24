# Register your models here.
from django.contrib import admin
from .models import Companies
from .views import model_list
from django.shortcuts import render
class companies_model(admin.ModelAdmin):
    list_display=['company_name','company_location','employee_no']
    

admin.site.register(Companies,companies_model)
