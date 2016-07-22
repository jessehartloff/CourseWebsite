from courses.models import Course, Content


def all_lessons(request):
    return {'all_lessons': Content.objects.all()}


def all_lectures(request):
    return {'all_lectures': Content.objects.all().filter(page_type='lecture').order_by('index')}


def all_assignments(request):
    return {'all_assignments': Content.objects.all().filter(page_type='assignment').order_by('index')}


def syllabus(request):
    return {'syllabus': Content.objects.all().filter(page_type='syllabus')}


def schedule(request):
    return {'schedule': Content.objects.all().filter(page_type='schedule')}
