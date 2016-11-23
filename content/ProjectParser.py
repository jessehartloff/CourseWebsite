import os
import django
import re

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseWebsite.settings")
django.setup()

from courses.models import Course, Group, Repository, Developer, Video, Extra

directory = "content/cse442-groups/"


class Group_O:
    def __init__(self, group_name):
        self.name = group_name
        self.members = []
        self.slack_channel = ""
        self.project_description = ""
        self.ta = ""
        self.repos = []
        self.videos = {}
        self.private = False
        self.has_extra = False
        self.extra = {}
        self.has_landing = False
        self.landing_link = ""


def parse_groups():
    group_file = directory + "groups"
    all_groups = {}
    all_with_duplicates = []
    all_students_in_groups = set([])
    group_objects = {}

    with open(group_file, "r") as groups:
        for line in groups:
            # for email in line.split(","):
            line = line.strip()
            if "\t" not in line:
                print("bad group format: " + str(line))
                continue
            if line[0] == '#':
                print("skipping: " + line)
                continue
            split_line = line.split("\t")
            group_name = split_line[0]
            group_members = split_line[1]
            this_group_members = []
            for member in group_members.split(","):
                member = member.strip().lower()
                if member in all_students_in_groups:
                    print("Too many groups foo! " + member)
                # all_with_duplicates.append(member)
                all_students_in_groups.add(member)
                this_group_members.append(member)
            if group_name in all_groups.keys():
                print("wtf " + group_name)
            this_group = Group_O(group_name)
            this_group.members = this_group_members
            group_objects[group_name] = this_group
            all_groups[group_name] = this_group_members
    print(str(len(all_groups)) + " groups")
    print(str(len(all_students_in_groups)) + " students in groups")
    # print(str(len(all_with_duplicates)) + " students with duplicates")
    return [all_students_in_groups, all_groups, group_objects]


def parse_group_descriptions(groups_objects):
    group_descriptions_file = directory + "group_descriptions"
    with open(group_descriptions_file, "r") as group_descriptions:
        for line in group_descriptions:
            if "\t" not in line:
                print("no tab found: " + str(line))
                continue
            line = line.strip()
            line_split = line.split("\t")
            group_name = line_split[0]
            group_slack = line_split[1]
            project_description = line_split[2]
            if group_name not in groups_objects:
                print("Not a real group: " + group_name)
                continue
            groups_objects[group_name].slack_channel = group_slack
            groups_objects[group_name].project_description = project_description


def parse_group_ta(groups_objects):
    group_ta_file = directory + "ta-groups.txt"
    with open(group_ta_file, "r") as group_ta:
        for line in group_ta:
            if "\t" not in line:
                print("no tab found: " + str(line))
                continue
            line = line.strip()
            line_split = line.split("\t")
            group_name = line_split[0]
            ta_ubit = line_split[1]
            if group_name not in groups_objects:
                print("Not a real group: " + group_name)
                continue
            groups_objects[group_name].ta = ta_ubit


def parse_group_repos(groups_objects):
    group_repo_file = directory + "AllRepos"
    with open(group_repo_file, "r") as group_repo:
        for line in group_repo.readlines():
            line = line.strip()
            # print(line)
            # print()
            line_split = line.split("\t")
            group_name = line_split[0].strip()
            repo_links = line_split[1].strip() if len(line_split) > 1 else "NO REPO"
            private = line_split[2].strip() if len(line_split) > 2 else ""
            if group_name not in groups_objects:
                print("Not a real group (Repos): " + group_name)
                continue
            # print(repo_links)
            groups_objects[group_name].repos = repo_links.split(";")
            if private == "Private":
                groups_objects[group_name].private = True


def parse_group_landing_pages(groups_objects):
    landing_pages_file = directory + "landing_pages"
    with open(landing_pages_file, "r") as landing_pages:
        for line in landing_pages.readlines():
            line = line.strip()
            # print(line)
            # print()
            line_split = line.split(",")
            group_name = line_split[0].strip()
            landing_link = line_split[1].strip()
            if group_name not in groups_objects:
                print("Not a real group (Landing Page): " + group_name)
                continue
            groups_objects[group_name].has_landing = True
            groups_objects[group_name].landing_link = landing_link


# source: http://stackoverflow.com/questions/4705996/python-regex-convert-youtube-url-to-youtube-video
def youtube_url_validation(url):
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    youtube_regex_match = re.match(youtube_regex, url)
    if youtube_regex_match:
        return youtube_regex_match.group(6)

    return youtube_regex_match


# end source

def parse_group_videos(groups_objects):
    group_video_file = directory + "AllVideos"
    with open(group_video_file, "r") as group_video:
        for line in group_video.readlines():
            # print(line)
            if "\t" not in line:
                print("no tab found: " + str(line))
                continue
            line = line.strip()
            line_split = line.split("\t")
            group_name = line_split[2]
            video_occasion = line_split[3]
            video_link = line_split[4]
            video_id = youtube_url_validation(video_link)
            if group_name not in groups_objects:
                print("Not a real group (Videos): " + group_name)
                continue
            groups_objects[group_name].videos[video_occasion] = video_id


def parse_extra(groups_objects, file, type):
    group_extra_file = directory + file
    with open(group_extra_file, "r") as group_extra:
        for line in group_extra.readlines():
            # print(line)
            if "," not in line:
                print("no comma found: " + str(line))
                continue
            line = line.strip()
            line_split = line.split(",")
            group_name = line_split[0].strip()
            extra_link = line_split[1].strip()
            if group_name not in groups_objects:
                print("Not a real group (Extra " + type + "): " + group_name)
                continue
            groups_objects[group_name].has_extra = True
            groups_objects[group_name].extra[type] = extra_link


def parse_files():
    [students_in_groups, groups, groups_o] = parse_groups()

    parse_group_descriptions(groups_o)
    parse_group_ta(groups_o)
    parse_group_repos(groups_o)
    parse_group_videos(groups_o)
    parse_extra(groups_o, "beta_testing", "Beta Testing")
    parse_extra(groups_o, "content_creation", "Content Creation")
    parse_group_landing_pages(groups_o)

    return groups_o


def process_projects(course_number):
    course = Course.objects.filter(course_number=course_number)
    if len(course) != 1:
        print("[Error] I only wanted one course: " + str(course_number))
        return
    course = course[0]
    course.course_project = True
    course.save()

    all_groups = parse_files()
    # Group.objects.all().delete()

    for group_o in all_groups.values():
        group = Group.objects.create(course=course)
        group.name = group_o.name
        group.slack_channel = group_o.slack_channel
        group.description = group_o.project_description
        group.ta = group_o.ta
        group.private = group_o.private
        group.has_extras = group_o.has_extra
        if group_o.has_landing:
            group.has_landing = True
            group.landing_link = group_o.landing_link
        for member in group_o.members:
            developer = Developer.objects.create(group=group)
            developer.ubit = member
            developer.save()
        for repo in group_o.repos:
            # print(repo)
            repository = Repository.objects.create(group=group)
            repository.link = repo
            repository.save()
        for [occasion, link] in group_o.videos.items():
            # print(group_o.name)
            # print(occasion)
            # print(link)
            # print()
            video = Video.objects.create(group=group)
            video.occasion = occasion
            video.link = link
            video.save()
        for [type, link] in group_o.extra.items():
            # print(group_o.name)
            # print(type)
            # print(link)
            # print()
            extra = Extra.objects.create(group=group)
            extra.type = type
            extra.link = link
            extra.save()
        group.save()

        # course = Course.objects.create(course_number=course_number, course_title=course_title)

# class Group:
#     def __init__(self, group_name):
#         self.name = group_name
#         self.members = []
#         self.slack_channel = ""
#         self.project_description = ""
#         self.ta = ""
#         self.repos = []
#         self.videos = {}
#         self.private = False
#
#
# class Group(models.Model):
#     course = models.ForeignKey(Course, blank=True, null=True)
#     name = models.CharField(max_length=100)
#     slack_channel = models.CharField(max_length=40)
#     description = models.TextField()
#     ta = models.CharField(max_length=100)
#     private = models.BooleanField(default=False)
#
# class Repository(models.Model):
#     group = models.ForeignKey(Group, blank=True, null=True)
#     link = models.CharField(max_length=100)
#
# class Developer(models.Model):
#     group = models.ForeignKey(Group, blank=True, null=True)
#     name = models.CharField(max_length=100)
#     ubit = models.CharField(max_length=20)
#
# class Video(models.Model):
#     group = models.ForeignKey(Group, blank=True, null=True)
#     occasion = models.CharField(max_length=20)
#     link = models.CharField(max_length=100)
