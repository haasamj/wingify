from django.shortcuts import render
from .models import wingifypass
# Create your views here.
def index(request):
    wing = wingifypass.objects.latest('id')
    context = {
        "hello":wing
        }
    return render(request, 'index.html', context)
