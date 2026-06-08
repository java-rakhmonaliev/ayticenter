from django.shortcuts import render
from .models import Photo


def gallery_index(request):
    photos = Photo.objects.all().order_by('order')
    return render(request, 'gallery/index.html', {'photos': photos})
