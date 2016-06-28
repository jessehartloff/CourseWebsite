import os
import django
import ContentParser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from lecture.models import Lesson, Section

lectures_directory = "lectures/"
assignments_directory = "assignments/"
extra_directory = "extra/"


def delete_all_lessons():
    Lesson.objects.all().delete()


def populate_file(file, page_type):
    print(file)
    ContentParser.parse_lesson(file, page_type)


def populate_directory(directory, page_type):
    for file in os.listdir(directory):
        populate_file(directory + file, page_type)


# def sort_lesson_type(page_type):
#     Lesson.objects.filter(page_type=page_type)


delete_all_lessons()
populate_directory(lectures_directory, 'lecture')
populate_directory(assignments_directory, 'assignment')

populate_file(extra_directory + 'syllabus.html', 'syllabus')
populate_file(extra_directory + 'schedule.html', 'schedule')

# sort_lesson_type('lecture')
# sort_lesson_type('assignment')
