# models.py
# Created by Egor Matveev
# 16.05.2021
from django.contrib.auth.models import User
from django.db import models


class Temperament(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(default='')
    variants = models.TextField(default='')
    block = models.IntegerField(null=True)

    @property
    def answers(self):
        if self.variants == '':
            return []
        return self.variants.split(';')

    def __str__(self):
        return self.text


class Attempt(models.Model):
    name = models.TextField(default='')
    grade = models.TextField(default='')
    group = models.TextField(default='')
    temperament = models.ForeignKey(Temperament, on_delete=models.SET_NULL, null=True)
    role = models.TextField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} | {self.temperament} | {self.role}'

    @property
    def answers(self):
        return FormAnswer.objects.filter(attempt=self)


class FormAnswer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    answer = models.TextField(default='')
