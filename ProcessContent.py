from content.addAllContent import process_course
import os

image_destination_directory = "static/courses/"

if not os.path.exists(image_destination_directory):
    os.makedirs(image_destination_directory)

# process_course('cse115', "Introduction to Computer Science", image_destination_directory)
# process_course('cse250', "Data Structures", image_destination_directory)
# process_course('cse404', "Web Development", image_destination_directory)
process_course('cse442', "Software Engineering", image_destination_directory)

