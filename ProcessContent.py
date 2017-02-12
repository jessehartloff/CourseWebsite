from content.addAllContent import process_course
from content.addAllContent import delete_all_courses
from content.ProjectParser import process_projects
import os

image_destination_directory = "static/courses/"

if not os.path.exists(image_destination_directory):
    os.makedirs(image_destination_directory)

delete_all_courses()
process_course('CSE115', "Introduction to Computer Science I", image_destination_directory)
# process_course('CSE312', "Web Development", image_destination_directory)
process_course('CSE442', "Software Engineering", image_destination_directory)
# process_course('P1', "Computer Science I", image_destination_directory)

# process_course('CSE250', "Data Structures", image_destination_directory)
# process_course('CSE442-Summer', "Software Engineering", image_destination_directory)

process_projects('CSE442')
