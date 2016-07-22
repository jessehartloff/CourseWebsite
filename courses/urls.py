from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<course_number>.+)/$', views.course_home, name='course_home'),
    url(r'^(?P<course_number>.+)/(?P<lecture_name>.+)/$', views.lecture, name='lecture'),
    url(r'^(?P<course_number>.+)/(?P<assignment_name>.+)/$', views.assignment, name='assignment'),
    url(r'^(?P<course_number>.+)/syllabus/$', views.syllabus, name='syllabus'),
    url(r'^(?P<course_number>.+)/schedule/$', views.schedule, name='schedule'),
    # url(r'^(?P<course_number>.+)/all_lecture/$', views.all_lecture, name='all_lecture'),
    url(r'^', views.index, name='index'),
]
