from django.shortcuts import render
from courses.models import Course
from .models import CareerPath


def career_index(request):
    courses_with_paths = []
    courses = Course.objects.filter(is_active=True, career_paths__isnull=False).distinct().order_by('order')
    for course in courses:
        paths = course.career_paths.all().order_by('order').prefetch_related('companies')
        if paths.exists():
            courses_with_paths.append({'course': course, 'paths': paths})
    return render(request, 'career/index.html', {'courses_with_paths': courses_with_paths})
