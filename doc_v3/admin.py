from .models import contact, appointment, department, prescription
from django.http import HttpResponse
from django.urls import path
from django.db import models
from django.shortcuts import render
from django.template.response import TemplateResponse

#from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


from django.contrib import admin



	

@admin.register(appointment)
class appointment(admin.ModelAdmin):
    list_display = ("app_id", "PatientName","AppointmentDate","PatientPhone","PatientEmail")
    search_fields = ["PatientName","AppointmentDate","PatientPhone","PatientEmail"]



@admin.register(prescription)
class prescriptionAdmin(admin.ModelAdmin):

    def get_app_details_PatientName(self, obj):
        return obj.app_id.PatientName
    def get_app_details_AppointmentDate(self, obj):
        return obj.app_id.AppointmentDate
    def print_prescription(self,request,queryset):
        print(queryset[0].medicines)  
        return render(request, "admin\doc_v3\prescription.html", context={'queryset':queryset})
    
    list_select_related = ['app_id__doc_id']
    autocomplete_fields = ['app_id']
    get_app_details_PatientName.admin_order_field  = 'prescription__appointment'
    get_app_details_AppointmentDate.admin_order_field  = 'prescription__appointment'
    list_display = ("pres_id", "get_app_details_PatientName","get_app_details_AppointmentDate",'medicines')
    actions = [print_prescription, ]    


@admin.register(department)
class department(admin.ModelAdmin):
    list_display = ("department_name", "doctor_name")

# Register your models here.
@admin.register(contact)
class contact(admin.ModelAdmin):
    list_display = ("Name", "Subject","Email")
    def has_module_permission(self,request):
        return True
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           key=2,
        )
        return TemplateResponse(request, "admin\doc_v3\index.html", context)

class DummyModel(models.Model):

    class Meta:
        verbose_name_plural = 'Print Prescription'
        app_label = 'doc_v3'

def my_custom_view(request):
    return render(request, 'admin\index.html')


class DummyModelAdmin(admin.ModelAdmin):
    model = contact
	
    def has_module_permission(self,request):
        return True
		
    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', my_custom_view, name=view_name),
        ]
#admin.site.register(DummyModel, DummyModelAdmin)


class MyModelAdmin(admin.ModelAdmin):
    def has_module_permission(self,request):
        return True
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.my_view),
        ]
        return my_urls + urls

    def my_view(self, request):
        # ...
        context = dict(
           # Include common variables for rendering the admin template.
           self.admin_site.each_context(request),
           # Anything else you want in the context...
           key=2,
        )
        return TemplateResponse(request, "admin\index.html", context)
		
admin.site.register(DummyModel, MyModelAdmin)
