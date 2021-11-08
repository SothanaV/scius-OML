from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myApp/home.html')

def profile(request):
    return render(request, 'myApp/profile.html')