# from django.http import Http404

from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Course, Content


def course_home(request, course_number):
    course = Course.objects.get(course_number=course_number)
    # should check if course was found

    a_list = Content.objects.filter(course=course)
    context = {'lesson_list': a_list, 'course': course}
    return render(request, 'courses/index.html', context)


def index(request):
    # course = Course.objects.get(course_number=course_number)
    # should check if course was found
    # a_list = Content.objects.filter(course=course)
    # context = {'lesson_list': a_list, 'course': course}
    return render(request, 'courses/index.html')


def all_lecture(request):
    return render(request, 'courses/lecture-all.html')


def lecture(request, lecture_name):
    this_lesson = Content.objects.get(title=lecture_name, page_type='lecture')
    context = {'this_lesson': this_lesson}
    return render(request, 'courses/lecture.html', context)


def assignment(request, assignment_name):
    this_lesson = Content.objects.get(title=assignment_name, page_type='assignment')
    context = {'this_lesson': this_lesson}
    return render(request, 'courses/assignment.html', context)


def syllabus(request):
    this_lesson = Content.objects.get(page_type='syllabus')
    context = {'this_lesson': this_lesson}
    return render(request, 'courses/syllabus.html', context)


def schedule(request):
    this_lesson = Content.objects.get(page_type='schedule')
    context = {'this_lesson': this_lesson}
    return render(request, 'courses/schedule.html', context)
