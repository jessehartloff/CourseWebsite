from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'^(?P<lecture_name>.+)/$', views.lecture, name='lecture'),
    url(r'^lecture/(?P<lecture_name>.+)/$', views.lecture, name='lecture'),
    url(r'^assignment/(?P<assignment_name>.+)/$', views.assignment, name='assignment'),
    url(r'^syllabus', views.syllabus, name='syllabus'),
    url(r'^schedule', views.schedule, name='schedule'),
    url(r'^all_lecture/$', views.all_lecture, name='all_lecture'),
    url(r'^', views.index, name='index'),
]
