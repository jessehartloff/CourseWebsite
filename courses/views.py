# from django.http import Http404
import subprocess

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from subprocess import call
from django.utils import timezone

from .forms import CommentForm

from .models import Course, Content, Comment


def comment_answered(request, course_number, comment_id):
    comment_object = Comment.objects.filter(comment_id=comment_id)[0]
    comment_object.time_answered = timezone.now()
    comment_object.answered = True
    comment_object.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render_content(request, course_number, 'schedule', 'courses/schedule.html')


def comment_form(request, course_number):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # comment_object = Comment.objects.create(comment_text=str(form.cleaned_data.get('comment_text')))
        # comment_object.save()

        # check whether it's valid:
        if form.is_valid():
            # jhvg;
            # form.cleaned_data.comment
            comment_object = Comment.objects.create(comment_text=str(form.cleaned_data.get("comment")))
            # comment_object.time_submitted = timezone.now()
            comment_object.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render_content(request, course_number, 'schedule', 'courses/schedule.html')
            # return HttpResponseRedirect('/learn/courses/' + str(course_number) + '/schedule/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render_content(request, course_number, 'schedule', 'courses/schedule.html')
    # return render(request, 'courses/schedule.html', {'form': form, 'course_number'})


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
    # comment_object = Comment.objects.create()
    # comment_object.comment_text = "hello!!"
    # comment_object.save()
    course = Course.objects.get(course_number=course_number)
    lectures = Content.objects.filter(course=course, page_type='lecture', index__gte=0).order_by('index')
    assignments = Content.objects.filter(course=course, page_type='assignment').order_by('index')
    this_lecture = Content.objects.get(course=course, page_type=page_type, short_title=short_title) if short_title != "" \
        else Content.objects.get(course=course, page_type=page_type)
    form = CommentForm()
    context = {'lectures': lectures, 'assignments': assignments, 'course': course, 'this_lecture': this_lecture,
               'form': form}
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


def sys_call(the_call):
    # print(the_call)
    result = subprocess.Popen(the_call.strip().split(" "), stdout=subprocess.PIPE).communicate()[0]
    result = result.decode("utf-8")
    return result


def hook(request, course_number):
    valid_courses = ["CSE442", "CSE442-Fall"]
    result = "no call"
    if course_number in valid_courses:
        result = sys_call("git pull")
        # call(["git", "pull"])
        # with open("junk.txt", "w") as output_file:
        #     output_file.write(str(request))
        # raise Http404("You really shouldn't be here: " + str(request))

    raise Http404("You really shouldn't be here: " + str(result))
