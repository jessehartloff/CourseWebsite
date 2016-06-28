from lecture.models import Lesson


def all_lessons(request):
    return {'all_lessons': Lesson.objects.all()}


def all_lectures(request):
    return {'all_lectures': Lesson.objects.all().filter(page_type='lecture').order_by('index')}


def all_assignments(request):
    return {'all_assignments': Lesson.objects.all().filter(page_type='assignment').order_by('index')}


def syllabus(request):
    return {'syllabus': Lesson.objects.all().filter(page_type='syllabus')}


def schedule(request):
    return {'schedule': Lesson.objects.all().filter(page_type='schedule')}
