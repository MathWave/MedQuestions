# admin.py
# Created by Egor Matveev
# 16.05.2021


from django.contrib import admin
from Main.models import Question, FormAnswer, Attempt, Temperament

admin.site.register(Question)
admin.site.register(FormAnswer)
admin.site.register(Attempt)
admin.site.register(Temperament)
