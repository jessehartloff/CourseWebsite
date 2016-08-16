from content.addAllContent import process_course
import os

image_destination_directory = "static/courses/"

if not os.path.exists(image_destination_directory):
    os.makedirs(image_destination_directory)

# process_course('CSE115', "Introduction to Computer Science", image_destination_directory)
# process_course('CSE250', "Data Structures", image_destination_directory)
# process_course('CSE404', "Web Development", image_destination_directory)
process_course('CSE442-Summer', "Software Engineering", image_destination_directory)
process_course('CSE442', "Software Engineering", image_destination_directory)


# It worked?!