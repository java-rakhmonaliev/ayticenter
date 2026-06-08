from django.shortcuts import render, get_object_or_404
from .models import Course


def course_list(request):
    courses = Course.objects.filter(is_active=True).order_by('order')
    return render(request, 'courses/list.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    career_paths = course.career_paths.all().order_by('order')
    teachers = course.teachers.filter(is_active=True).order_by('order')
    return render(request, 'courses/detail.html', {
        'course': course,
        'career_paths': career_paths,
        'teachers': teachers,
    })
