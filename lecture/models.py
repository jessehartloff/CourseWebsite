from django.db import models
import datetime
from django.utils import timezone


class Lesson(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Section(models.Model):
    lesson = models.ForeignKey(Lesson)
    sectionTitle = models.CharField(max_length=100)
    index = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.sectionTitle


# class Activity(models.Model):
#     section = models.ForeignKey(Section)


class Assignment(models.Model):
    title = models.CharField(max_length=100)


class AssignmentPart(models.Model):
    assignment = models.ForeignKey(Assignment)
    text = models.TextField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_test
