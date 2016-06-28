from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    page_type = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.CharField(max_length=200, blank=True, null=True)
    # next_lesson = models.ForeignKey('self', blank=True, null=True)
    next_lesson_title = models.CharField(max_length=100, blank=True, null=True)
    previous_lesson_title = models.CharField(max_length=100, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    lesson = models.ForeignKey(Lesson, blank=True, null=True)
    sectionTitle = models.CharField(max_length=100)
    index = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.sectionTitle
