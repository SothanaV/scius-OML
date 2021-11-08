from django.urls import path
from .views import home, profile

app_name = "myApp"

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile, name='profile')
]
