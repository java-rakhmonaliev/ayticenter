from django.shortcuts import render
from .models import SiteSettings
from courses.models import Course
from teachers.models import Teacher
from news.models import Post


def home(request):
    settings = SiteSettings.get()
    active_courses = Course.objects.filter(is_active=True).order_by('order')
    courses = active_courses[:6]
    teachers = Teacher.objects.filter(is_active=True).order_by('order')[:4]
    latest_news = Post.objects.filter(is_published=True).order_by('-published_at')[:3]
    typed_words = [w.strip() for w in settings.hero_typed_words.split(',') if w.strip()]
    if not typed_words:
        typed_words = [c.name for c in active_courses]
    return render(request, 'core/home.html', {
        'settings': settings,
        'courses': courses,
        'course_count': active_courses.count(),
        'typed_words': typed_words,
        'teachers': teachers,
        'latest_news': latest_news,
    })


def about(request):
    settings = SiteSettings.get()
    return render(request, 'core/about.html', {
        'settings': settings,
    })
