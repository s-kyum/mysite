from django.contrib import admin

# 모델 등록

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

