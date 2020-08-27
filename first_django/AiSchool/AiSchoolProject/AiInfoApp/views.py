from django.shortcuts import render
from .models import classes

# Create your views here.
def home(request):
    class_object = classes.objects.all()

    context = {'class_object': class_object}
    return render(request, 'home.html', context)