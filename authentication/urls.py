from django.urls import path, include
from .views import signup_view, login_view, logout_view

app_name = 'authentication'

urlpatterns = [
    path('signup', signup_view, name='signup_view'),
    path('login', login_view, name='login_view'),
    path('logout', logout_view, name='logout_view'),
    path('', include('hospital.urls', namespace='hospital')),
]
