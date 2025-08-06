from django.contrib import admin
from .models import Hospital, Department, Doctor, Doctor_Profile, Patient, Patient_Profile, Appointment, Medical_Record
# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    list_display=['id','hname','hcity']
    list_display_links=['hname']
    ordering=['id']

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','dname','d_loc','hospital']
    list_display_links=['dname']
    ordering=['id']

class DoctorAdmin(admin.ModelAdmin):
    list_display=['id','dname','dspecialization','Department']
    list_display_links=['dname']
    ordering=['id']

class Doctor_Profile_Admin(admin.ModelAdmin):
    list_display=['id','dcontact','dage','dmail','doctor']
    list_display_links=['doctor']
    ordering=['id']

class PatientAdmin(admin.ModelAdmin):
    list_display=['id','pname','page','Doctor']
    list_display_links=['pname','Doctor']
    ordering=['id']

class Patient_Profile_Admin(admin.ModelAdmin):
    list_display=['id','pcontact','pmail','p_address','patient']
    list_display_links=['patient']
    ordering=['id']

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','appointment_date','appointment_time','patient','doctor']
    list_display_links=['patient','doctor']
    ordering=['id']

class Medical_Record_Admin(admin.ModelAdmin):
    list_display=['id','record_date','diagnosis','treatment','patient','doctor']
    list_display_links=['patient','doctor']
    ordering=['id']

admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Doctor_Profile,Doctor_Profile_Admin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Patient_Profile,Patient_Profile_Admin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Medical_Record,Medical_Record_Admin)