from django.contrib import admin
from .models import pollah_question, pollah_answer
# Register your models here.


class answer(admin.TabularInline):
    model = pollah_answer
    extra = 3

class questionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['time_created'], 'classes':['collapse']}),
    ]
    inlines = [answer]
    list_display = ('question_text', 'time_created')
    list_filter = ['time_created']
    search_fields = ['question_text']

admin.site.register(pollah_question, questionAdmin)