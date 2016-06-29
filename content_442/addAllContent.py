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
        if file.find(".DS_Store") != -1:
            continue
        populate_file(directory + file, page_type)


def sort_lesson_type(page_type):
    Lesson.objects.filter(page_type=page_type)
    lesson = Lesson.objects.filter(page_type=page_type, previous_lesson_title="none")
    if len(lesson) == 0:
        print("Warning: No " + str(page_type) + " with previous of 'none'")
    if len(lesson) != 1:
        print("Warning: More than one " + str(page_type) + " with previous of 'none'")
    only_lesson = lesson[0]
    current_index = 0
    only_lesson.index = current_index
    current_index += 1
    only_lesson.save()

    while only_lesson.next_lesson_title != 'none':
        lesson = Lesson.objects.filter(page_type=page_type, title=only_lesson.next_lesson_title)
        if len(lesson) == 0:
            print("Warning: No " + str(page_type) + " with title of " + str(only_lesson.next_lesson_title))
            break
        if len(lesson) != 1:
            print("Warning: More than one " + str(page_type) + " with title of " + str(only_lesson.next_lesson_title))
        only_lesson = lesson[0]
        only_lesson.index = current_index
        current_index += 1
        only_lesson.save()


delete_all_lessons()
populate_directory(lectures_directory, 'lecture')
populate_directory(assignments_directory, 'assignment')

populate_file(extra_directory + 'syllabus.html', 'syllabus')
populate_file(extra_directory + 'schedule.html', 'schedule')

sort_lesson_type('lecture')
sort_lesson_type('assignment')
