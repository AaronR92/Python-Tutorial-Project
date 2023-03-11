from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            'classes': ['collapse'],
        }),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInLine]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 20


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.site_header = 'Polls administration'
