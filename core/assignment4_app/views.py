from django.shortcuts import render
from assignment4_app import models
# Create your views here.

def home(request):
    data = models.Product.objects.all()
    return render(request, 'base.html', {'data': data})