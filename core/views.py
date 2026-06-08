from django.shortcuts import render
from .models import SiteSettings
from courses.models import Course
from teachers.models import Teacher
from news.models import Post


def home(request):
    settings = SiteSettings.get()
    courses = Course.objects.filter(is_active=True).order_by('order')[:4]
    teachers = Teacher.objects.filter(is_active=True).order_by('order')[:4]
    latest_news = Post.objects.filter(is_published=True).order_by('-published_at')[:2]
    return render(request, 'core/home.html', {
        'settings': settings,
        'courses': courses,
        'teachers': teachers,
        'latest_news': latest_news,
    })


def about(request):
    settings = SiteSettings.get()
    return render(request, 'core/about.html', {
        'settings': settings,
    })
