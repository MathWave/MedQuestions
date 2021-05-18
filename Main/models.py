# models.py
# Created by Egor Matveev
# 16.05.2021


from django.db import models


class Question(models.Model):
    text = models.TextField(default='')
    variants = models.TextField(default='')
    is_role = models.BooleanField(default=False)

    @property
    def answers(self):
        if self.variants == '':
            return []
        return self.variants.split(';')

    def __str__(self):
        return self.text


class Attempt(models.Model):
    surname = models.TextField(default='')
    name = models.TextField(default='')
    middle_name = models.TextField(default='')
    group = models.TextField(default='')
    temperament = models.TextField(default='')
    role = models.TextField(default='')

    def __str__(self):
        return f'{self.group} | {self.surname} {self.name} {self.middle_name} | {self.temperament} {self.role}'

    @property
    def answers(self):
        return FormAnswer.objects.filter(attempt=self)


class FormAnswer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.TextField(default='')
