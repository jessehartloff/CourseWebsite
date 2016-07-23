import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from courses.models import Course, Content, Section


def parse_variable(line):
    colon = line.find(':')
    if colon == -1:
        return ['']
    return [line[:colon].strip(), line[colon+1:].strip()]


def parse_lesson(course, filename, page_type):

    with open(filename) as file_content:
        lesson = Content.objects.create(course=course)
        lesson.page_type = page_type

        state = 'normal'
        section_index = 0

        for line in file_content:
            line = line.strip()

            if state == 'normal':

                # if line.startswith("==="):
                #     lesson.title = line[4:].strip()

                if line.startswith("=="):
                    if section_index != 0:
                        current_section.save()
                    current_section = Section.objects.create(index=section_index)
                    section_index += 1
                    current_section.lesson = lesson
                    current_section.sectionTitle = line[3:].strip()
                    current_section.html_content = ""

                elif line.startswith("="):
                    # subsection called line[2:].strip()
                    pass

                elif line.startswith("[.python_example]"):
                    # read between the "--"'s
                    pass

                elif line.startswith("---"):
                    state = 'variables'

                elif section_index != 0:
                    current_section.html_content += line

            elif state == 'variables':
                if line.startswith("---"):
                    state = 'normal'
                else:
                    result = parse_variable(line)
                    if len(result) == 2:
                        if result[0] == 'title':
                            lesson.title = result[1]
                        if result[0] == 'short_title':
                            lesson.short_title = result[1]
                        if result[0] == 'next_content_short':
                            lesson.next_content_short_title = result[1]
                        if result[0] == 'previous_content_short':
                            lesson.previous_content_short_title = result[1]
                        if result[0] == 'due_date':
                            lesson.due_date = result[1]

        if section_index != 0:
            current_section.save()

        lesson.save()
