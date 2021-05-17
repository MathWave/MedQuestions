from django.contrib import admin
from Main.models import Question, FormAnswer, Attempt

admin.site.register(Question)
admin.site.register(FormAnswer)
admin.site.register(Attempt)
