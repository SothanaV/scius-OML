from django.urls import path
from .views import home, profile, list_item, retrive_item, list_category, retrive_category, delete_category

app_name = "myApp"

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile, name='profile'),
    path('category', list_category, name='list-category'),
    path('category/<int:pk>/', retrive_category, name='retrive-category'),
    path('category/delete/<int:pk>/', delete_category, name='delete-category'),
    path('item', list_item, name='list-item'),
    path('item/<int:pk>/', retrive_item, name='retrive-item')
    
]
