from django.shortcuts import render, redirect
from courses.models import Course
from .forms import ApplicationForm


def apply(request):
    course_slug = request.GET.get('course', '')
    initial = {}

    if course_slug:
        try:
            course = Course.objects.get(slug=course_slug, is_active=True)
            initial['course'] = course
        except Course.DoesNotExist:
            pass

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admissions:success')
    else:
        form = ApplicationForm(initial=initial)

    return render(request, 'admissions/apply.html', {'form': form})


def success(request):
    return render(request, 'admissions/success.html')
