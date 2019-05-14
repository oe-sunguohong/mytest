from django.contrib import admin
from blog.models import *
# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']}),

    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Article)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)