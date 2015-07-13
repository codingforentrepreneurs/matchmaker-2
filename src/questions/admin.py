from django.contrib import admin

# Register your models here.

from .models import Question, Answer, UserAnswer


class AnswerTabularInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
	inlines = [AnswerTabularInline]
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)



admin.site.register(Answer)

admin.site.register(UserAnswer)