# from django.http import Http404

from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Course, Content


def course_home(request, course_number):
    course = Course.objects.get(course_number=course_number)
    # should check if course was found
    lectures = Content.objects.filter(course=course, page_type='lecture').order_by('index')
    assignments = Content.objects.filter(course=course, page_type='assignment').order_by('index')
    context = {'lectures': lectures, 'assignments': assignments, 'course': course}
    return render(request, 'courses/index.html', context)


def index(request):
    # TODO: road map of courses
    # course = Course.objects.get(course_number=course_number)
    # should check if course was found
    # a_list = Content.objects.filter(course=course)
    # context = {'lesson_list': a_list, 'course': course}
    return render(request, 'courses/index.html')
    # return render(request, 'faculty_page.html')


def render_content(request, course_number, page_type, template, short_title=""):
    course = Course.objects.get(course_number=course_number)
    lectures = Content.objects.filter(course=course, page_type='lecture').order_by('index')
    assignments = Content.objects.filter(course=course, page_type='assignment').order_by('index')
    this_lecture = Content.objects.get(course=course, page_type=page_type, short_title=short_title) if short_title != "" \
        else Content.objects.get(course=course, page_type=page_type)
    context = {'lectures': lectures, 'assignments': assignments, 'course': course, 'this_lecture': this_lecture}
    return render(request, template, context)


def lecture(request, course_number, lecture_short_title):
    return render_content(request, course_number, 'lecture', 'courses/lecture.html', lecture_short_title)
    # course = Course.objects.get(course_number=course_number)
    # this_lecture = Content.objects.get(course=course, title=lecture_short_title, page_type='lecture')
    # context = {'course': course, 'this_lecture': this_lecture}
    # return render(request, 'courses/lecture.html', context)


def assignment(request, course_number, assignment_short_title):
    return render_content(request, course_number, 'assignment', 'courses/assignment.html', assignment_short_title)
    # course = Course.objects.get(course_number=course_number)
    # this_assignment = Content.objects.get(course=course, title=assignment_short_title, page_type='assignment')
    # context = {'course': course, 'this_assignment': this_assignment}
    # return render(request, 'courses/assignment.html', context)


def syllabus(request, course_number):
    return render_content(request, course_number, 'syllabus', 'courses/syllabus.html')
    # course = Course.objects.get(course_number=course_number)
    # this_lesson = Content.objects.get(course=course, page_type='syllabus')
    # context = {'course': course, 'this_lesson': this_lesson}
    # return render(request, 'courses/syllabus.html', context)


def schedule(request, course_number):
    return render_content(request, course_number, 'schedule', 'courses/schedule.html')
    # course = Course.objects.get(course_number=course_number)
    # this_lesson = Content.objects.get(course=course, page_type='schedule')
    # context = {'course': course, 'this_lesson': this_lesson}
    # return render(request, 'courses/schedule.html', context)
