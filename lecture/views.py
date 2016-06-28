from django.http import Http404

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Lesson, Section

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'


from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader


def index(request):
    a_list = Lesson.objects.all()
    context = {'lesson_list': a_list}
    return render(request, 'lecture/index.html', context)


def lecture(request, lecture_name):
    this_lesson = Lesson.objects.get(title=lecture_name, page_type='lecture')
    context = {'this_lesson': this_lesson}
    return render(request, 'lecture/lecture.html', context)


def assignment(request, assignment_name):
    this_lesson = Lesson.objects.get(title=assignment_name, page_type='assignment')
    context = {'this_lesson': this_lesson}
    return render(request, 'lecture/assignment.html', context)


def syllabus(request):
    this_lesson = Lesson.objects.get(page_type='syllabus')
    context = {'this_lesson': this_lesson}
    return render(request, 'lecture/syllabus.html', context)


def schedule(request):
    this_lesson = Lesson.objects.get(page_type='schedule')
    context = {'this_lesson': this_lesson}
    return render(request, 'lecture/schedule.html', context)
