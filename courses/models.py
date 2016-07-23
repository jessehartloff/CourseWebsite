from __future__ import print_function
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    course_number = models.CharField(max_length=10, blank=True, null=True)
    course_title = models.CharField(max_length=100, blank=True, null=True)


class Content(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=40, blank=True, null=True)
    page_type = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=200, blank=True, null=True)

    # ordering variables
    next_content_short_title = models.CharField(max_length=100, blank=True, null=True)
    previous_content_short_title = models.CharField(max_length=100, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    lesson = models.ForeignKey(Content, blank=True, null=True)
    sectionTitle = models.CharField(max_length=100)
    index = models.IntegerField()
    html_content = models.TextField()

    class Meta:
        ordering = ['index']

    def __str__(self):
        return self.sectionTitle
