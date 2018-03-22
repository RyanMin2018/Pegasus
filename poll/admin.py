from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, PollAdmin)
#admin.site.register(PollChoice)