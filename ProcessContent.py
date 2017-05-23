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
process_course('cse115-f17', "CSE115", "Introduction to Computer Science", media_destination_directory)
process_course('cse115-s17', "CSE115", "Introduction to Computer Science", media_destination_directory, True)
process_course('cse312-s18', "CSE312", "Web Applications", media_destination_directory)
# process_course('cse442-fall2017', "Software Engineering", media_destination_directory)
process_course('cse442-f17', "CSE442", "Software Engineering", media_destination_directory)
process_course('cse442-f16', "CSE442", "Software Engineering", media_destination_directory, True)
# process_course('P1', "Computer Science I", media_destination_directory)

# process_course('cse250', "Data Structures", media_destination_directory)
# process_course('cse442-Summer', "Software Engineering", media_destination_directory)

process_projects('cse442-f16')
process_projects('cse442-f17')
