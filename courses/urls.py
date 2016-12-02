from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<course_number>.+)/index/$', views.course_home, name='course_home'),
    url(r'^(?P<course_number>.+)/lectures/(?P<lecture_short_title>.+)/$', views.lecture, name='lecture'),
    url(r'^(?P<course_number>.+)/assignments/(?P<assignment_short_title>.+)/$', views.assignment, name='assignment'),
    url(r'^(?P<course_number>.+)/syllabus/$', views.syllabus, name='syllabus'),
    url(r'^(?P<course_number>.+)/schedule/$', views.schedule, name='schedule'),
    url(r'^(?P<course_number>.+)/resources/$', views.resources, name='resources'),
    url(r'^(?P<course_number>.+)/projects/all/$', views.projects, name='projects'),
    url(r'^(?P<course_number>.+)/projects/(?P<project_id>.+)/$', views.project, name='project'),
    url(r'^(?P<course_number>.+)/hook/$', views.hook, name='hook'),
    url(r'^(?P<course_number>.+)/hook$', views.hook, name='hook2'),
    url(r'^(?P<course_number>.+)/comment_form/', views.comment_form, name='comment_form'),
    url(r'^(?P<course_number>.+)/comment_answered/(?P<comment_id>.+)', views.comment_answered, name='comment_answered'),
    # url(r'^(?P<course_number>.+)/all_lecture/$', views.all_lecture, name='all_lecture'),
    url(r'^', views.index, name='index'),
]
