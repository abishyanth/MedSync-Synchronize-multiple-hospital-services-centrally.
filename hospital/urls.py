from django.urls import path, include
from . import views

app_name = 'hospital'

urlpatterns= [
    path('', views.hospitals, name='hospitals'),
    path('hospitals/<int:hospital_id>/', views.hospital_detail_view, name='hospital_detail'),
    path('hospital/<int:hospital_id>/doctors/', views.doctor_list_view, name='doctor_list'),
    path('hospital/<int:hospital_id>/patients/', views.patient_list_view, name='patient_list'),
    path('patient/<int:patient_id>/profile/', views.patient_profile_view, name='patient_profile'),
    path('doctor/<int:doctor_id>/profile/', views.doctor_profile_view, name='doctor_profile'),
    path('add_hospital/', views.add_hospital, name='add_hospital'),
    path('add_doctor/<int:hospital_id>/', views.add_docotor, name='add_doctor'),
    path('add_patient/<int:doctor_id>/', views.add_patient, name='add_patient'),
    path('add_department/<int:hospital_id>/', views.add_Department, name='add_department'),
    path('remove_patient/<int:patient_id>/', views.remove_patient, name='remove_patient'),
]