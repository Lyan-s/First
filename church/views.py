from django.shortcuts import render
from .models import ChurchDetails

# Create your views here.
def home(request):
    details = ChurchDetails.objects.first()
    return render(request, "church/home.html", {"details": details})
