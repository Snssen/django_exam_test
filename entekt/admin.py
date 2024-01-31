from django.contrib import admin
from .models import Subject, Course, Module, Quest, Option, CorrectAnswer


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('qno', 'question',)
    search_fields = ('qno', 'question',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('quest', 'option_letter', 'option',)
    list_filter = ('quest',)
    search_fields = ('quest__question', 'option_letter', 'option',)


@admin.register(CorrectAnswer)
class CorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'quest', 'correct_option',)
    list_filter = ('quest',)  # Optional: filter options
    search_fields = ('quest__question_text',)  # Optional: add fields for search
