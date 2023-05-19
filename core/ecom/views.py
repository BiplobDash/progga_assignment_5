from django.shortcuts import render
from ecom import models
# Create your views here.

def home(request):
    data = models.Student.objects.all()
    return render(request, 'base.html', {'data': data})
