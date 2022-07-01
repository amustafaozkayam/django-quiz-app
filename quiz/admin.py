from django.contrib import admin
from .models import *
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin


class AnswersInline(SuperInlineModelAdmin, admin.TabularInline):
    model = Answers
    extra = 4

class QuestionInline(SuperInlineModelAdmin, admin.StackedInline):
    model = Questions
    extra = 1
    inlines = [AnswersInline]


class QuizAdmin(SuperModelAdmin):
    model = Quiz
    inlines = [QuestionInline]


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'is_right')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'title', 'difficulty')
    inlines = [AnswersInline]


# Register your models here.
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)