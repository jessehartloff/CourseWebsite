import os
import django
import ContentParser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from lecture.models import Lesson, Section, Assignment, AssignmentPart

lectures_directory = "lectures"


def delete_all_lectures():
    Lesson.objects.all().delete()


def populate_lectures():
    for file in os.listdir(lectures_directory):
        print(file)
        full_path = lectures_directory + "/" + file
        ContentParser.parse_lesson(full_path)


delete_all_lectures()
populate_lectures()
# ContentParser.parse_lesson("lectures/1-Syntax.html")
