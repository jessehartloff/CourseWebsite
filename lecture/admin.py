from django.contrib import admin
from .models import Choice, Question, Lesson, Section, Assignment, AssignmentPart
# admin.site.register(Question)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class SectionInline(admin.TabularInline):
    model = Section
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [SectionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)