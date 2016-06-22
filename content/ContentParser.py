import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from lecture.models import Lesson, Section, Assignment, AssignmentPart


def parse_lesson(filename):
    with open(filename) as file_content:
        lesson = Lesson.objects.create()

        section_index = 0
        for line in file_content:
            line = line.strip()

            if line.startswith("==="):
                lesson.title = line[4:].strip()

            elif line.startswith("=="):
                if section_index != 0:
                    current_section.save()
                current_section = Section.objects.create(index=section_index)
                section_index += 1
                current_section.lesson = lesson
                current_section.sectionTitle = line[3:].strip()
                current_section.content = ""

            elif line.startswith("="):
                # subsection called line[2:].strip()
                pass

            elif line.startswith("[.python_example]"):
                # read between the "--"'s
                pass
            elif section_index != 0:
                current_section.content += line

        if section_index != 0:
            current_section.save()

        lesson.save()
