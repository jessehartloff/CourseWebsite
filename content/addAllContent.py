import os
import django
import ContentParser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from courses.models import Course, Content

lectures_directory = "lectures/"
assignments_directory = "assignments/"
extra_directory = "extra/"


def delete_course(course_number):
    Course.objects.filter(course_number=course_number).delete()
    # course = Course.objects.get(course_number=course_number)
    # Content.objects.filter(course=course).delete()


def populate_file(course, the_file, page_type):
    print(course.course_number + ": " + the_file)
    ContentParser.parse_lesson(course, the_file, page_type)


def populate_directory(course, directory, page_type):
    for the_file in os.listdir("content/" + course.course_number + "/" + directory):
        populate_file(course, "content/" + course.course_number + "/" + directory + the_file, page_type)


def sort_lesson_type(course, page_type):
    pass
    # Lesson.objects.filter(page_type=page_type)
    # lesson = Lesson.objects.filter(page_type=page_type, previous_lesson_title="none")
    # if len(lesson) == 0:
    #     print("Warning: No " + str(page_type) + " with previous of 'none'")
    # if len(lesson) != 1:
    #     print("Warning: More than one " + str(page_type) + " with previous of 'none'")
    # only_lesson = lesson[0]
    # current_index = 0
    # only_lesson.index = current_index
    # current_index += 1
    # only_lesson.save()
    #
    # while only_lesson.next_lesson_title != 'none':
    #     lesson = Lesson.objects.filter(page_type=page_type, title=only_lesson.next_lesson_title)
    #     if len(lesson) == 0:
    #         print("Warning: No " + str(page_type) + " with title of " + str(only_lesson.next_lesson_title))
    #         break
    #     if len(lesson) != 1:
    #         print("Warning: More than one " + str(page_type) + " with title of " + str(only_lesson.next_lesson_title))
    #     only_lesson = lesson[0]
    #     only_lesson.index = current_index
    #     current_index += 1
    #     only_lesson.save()


def process_course(course_number, course_title):

    delete_course(course_number)

    course = Course.objects.create(course_number=course_number, course_title=course_title)

    populate_directory(course, lectures_directory, 'lecture')
    populate_directory(course, assignments_directory, 'assignment')

    populate_file(course, "content/" + course.course_number + "/" + extra_directory + 'syllabus.html', 'syllabus')
    populate_file(course, "content/" + course.course_number + "/" + extra_directory + 'schedule.html', 'schedule')

    sort_lesson_type(course, 'lecture')
    sort_lesson_type(course, 'assignment')

    course.save()

#
# class Course(models.Model):
#     course_number = models.CharField(max_length=10, blank=True, null=True)
#     course_title = models.CharField(max_length=100, blank=True, null=True)
#
#
# class Content(models.Model):
#     course = models.ForeignKey(Course)
#     short_title = models.CharField(max_length=40, blank=True, null=True)
#     title = models.CharField(max_length=100)
#     page_type = models.CharField(max_length=100, blank=True, null=True)
#     due_date = models.CharField(max_length=200, blank=True, null=True)
#     next_content_short_title = models.CharField(max_length=100, blank=True, null=True)
#     previous_content_short_title = models.CharField(max_length=100, blank=True, null=True)
#     index = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return self.title
#
#
# class Section(models.Model):
#     lesson = models.ForeignKey(Content, blank=True, null=True)
#     sectionTitle = models.CharField(max_length=100)
#     index = models.IntegerField()
#     html_content = models.TextField()
#
#     def __str__(self):
#         return self.sectionTitle
