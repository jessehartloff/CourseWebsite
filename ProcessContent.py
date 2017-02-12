from content.addAllContent import process_course
from content.addAllContent import delete_all_courses
from content.ProjectParser import process_projects
from content.addAllContent import copy_common_media
import os

media_destination_directory = "static/courses/"

if not os.path.exists(media_destination_directory):
    os.makedirs(media_destination_directory)

delete_all_courses()

copy_common_media(media_destination_directory)
process_course('CSE115', "Introduction to Computer Science", media_destination_directory)
# process_course('CSE312', "Web Development", media_destination_directory)
process_course('CSE442', "Software Engineering", media_destination_directory)
# process_course('P1', "Computer Science I", media_destination_directory)

# process_course('CSE250', "Data Structures", media_destination_directory)
# process_course('CSE442-Summer', "Software Engineering", media_destination_directory)

process_projects('CSE442')
