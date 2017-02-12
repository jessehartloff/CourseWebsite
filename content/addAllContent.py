import os
import django
import ContentParser
import shutil
import distutils.dir_util

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from courses.models import Course, Content, Comment

content_directory = "content/"

assignments_directory = "assignments/"
extra_directory = "extra/"
lectures_directory = "lectures/"
image_directory = "media/"

media_directory = content_directory + "common_media"


def copy_common_media(destination_directory):
    distutils.dir_util.copy_tree(media_directory, destination_directory)


def delete_all_courses():
    # pass
    Course.objects.all().delete()


def delete_course(course_number):
    Course.objects.filter(course_number=course_number).delete()


def populate_file(course, the_file, page_type):
    print(course.course_number + ": " + the_file)
    ContentParser.parse_lesson(course, the_file, page_type)


# def populate_extra_directory(course, directory):
#     for the_file in os.listdir(content_directory + course.course_number.lower() + "/" + directory):
#         populate_file(course, content_directory + course.course_number.lower() + "/" + directory + the_file, "extra")


def populate_directory(course, directory, page_type):
    for the_file in os.listdir(content_directory + course.course_number.lower() + "/" + directory):
        populate_file(course, content_directory + course.course_number.lower() + "/" + directory + the_file, page_type)


def sort_lesson_type(course, page_type):
    # pass
    # Content.objects.filter(page_type=page_type, course=course)
    lesson = Content.objects.filter(page_type=page_type,
                                    course=course,
                                    previous_content_short_title="none")
    if len(lesson) == 0:
        print("Warning: No " + str(page_type) + " with previous of 'none'")
    if len(lesson) != 1:
        print("Warning: More than one " + str(page_type) + " with previous of 'none'")
    only_lesson = lesson[0]
    current_index = 0
    only_lesson.index = current_index
    current_index += 1
    only_lesson.save()

    while only_lesson.next_content_short_title != 'none':
        lesson = Content.objects.filter(page_type=page_type,
                                        course=course,
                                        short_title=only_lesson.next_content_short_title)
        if len(lesson) == 0:
            print("Warning: No " + str(page_type) + " with title of " + str(only_lesson.next_content_short_title))
            break
        if len(lesson) != 1:
            print(
                "Warning: More than one " + str(page_type) + " with title of " + str(
                    only_lesson.next_content_short_title))
        only_lesson = lesson[0]
        only_lesson.index = current_index
        current_index += 1
        only_lesson.save()


def copy_files(course, source_directory, destination_directory):
    distutils.dir_util.copy_tree(content_directory + course.course_number.lower() + "/" + source_directory, destination_directory)


def process_course(course_number, course_title, image_destination_directory):
    delete_course(course_number)

    # comments = Comment.objects.all()
    # comments.delete()

    # comment_object = Comment.objects.create(comment_text="Howdy!")
    # comment_object.save()

    course = Course.objects.create(course_number=course_number, course_title=course_title)

    populate_directory(course, lectures_directory, 'lecture')
    populate_directory(course, assignments_directory, 'assignment')
    populate_directory(course, extra_directory, 'extra')

    # populate_file(course, content_directory + course.course_number.lower() + "/" + extra_directory + 'syllabus.html',
    #               'syllabus')
    # populate_file(course, content_directory + course.course_number.lower() + "/" + extra_directory + 'schedule.html',
    #               'schedule')
    # populate_file(course, content_directory + course.course_number.lower() + "/" + extra_directory + 'resources.html',
    #               'resources')
    # populate_file(course, content_directory + course.course_number.lower() + "/" + extra_directory + 'assistance.html',
    #               'assistance')

    sort_lesson_type(course, 'lecture')
    sort_lesson_type(course, 'assignment')
    sort_lesson_type(course, 'extra')

    course.save()

    copy_files(course, image_directory, image_destination_directory)
