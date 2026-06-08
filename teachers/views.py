from django.shortcuts import render, get_object_or_404
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.filter(is_active=True).order_by('order')
    return render(request, 'teachers/list.html', {'teachers': teachers})


def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug, is_active=True)
    courses = teacher.courses.filter(is_active=True)
    return render(request, 'teachers/detail.html', {
        'teacher': teacher,
        'courses': courses,
    })
