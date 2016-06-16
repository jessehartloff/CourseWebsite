from lecture.models import Lesson


def all_lessons(request):
    return {'all_lessons': Lesson.objects.all()}
