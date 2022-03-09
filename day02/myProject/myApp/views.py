from django.shortcuts import render, redirect
from .models import Category, Item

# Create your views here.
def home(request):
    return render(request, 'myApp/home.html')

def profile(request):
    return render(request, 'myApp/profile.html')

def list_category(request):
    if request.method == "POST":
        data = request.POST
        Category.objects.create(
            name = data['name']
        )
    categoys = Category.objects.filter(is_use=True)
    context = {
        'categorys': categoys
    }
    return render(request=request, template_name='myApp/category-list.html', context=context)

def retrive_category(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == "POST":
        data = request.POST
        category.name = data['name']
        category.save()
    context = {
        'category': category
    }
    return render(request=request, template_name='myApp/category-retrive.html', context=context)

def delete_category(request, pk):
    catrgory = Category.objects.get(id=pk)
    catrgory.is_use=False
    catrgory.save()
    return redirect('myApp:list-category')
    

def list_item(request):
    context = {
        'items': Item.objects.filter(is_use=True),
        'categorys': Category.objects.filter(is_use=True)
    }
    return render(request=request, template_name='myApp/item-list.html', context=context)

def retrive_item(request, pk):
    item = Item.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request=request, template_name='myApp/item-retrive.html', context=context)