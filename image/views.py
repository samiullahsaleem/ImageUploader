from django.shortcuts import render
from .form import imageForm
from .models import image
from django.utils import timezone

timestamp = int(timezone.now().timestamp())
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = imageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = imageForm()
    images = image.objects.all()
    return render(request, 'image/home.html',{'form':form, 'images':images, 'timestamp':timestamp})
