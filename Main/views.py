# views.py
# Created by Egor Matveev
# 16.05.2021


from os import remove

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from Main.sync import synchronized_method
import matplotlib.pyplot as plt

# Create your views here.
from Main.models import Question, FormAnswer, Attempt, Temperament


def calc_info(attempt, answers):
    temp_ans = [ans.answer for ans in answers if not ans.question.block]
    a = ['Да', 'Нет']
    temp_ans = [
        1 if temp_ans[0] == a[0] else 0,
        1 if temp_ans[1] == a[0] else 0,
        1 if temp_ans[2] == a[0] else 0,
        1 if temp_ans[3] == a[0] else 0,
        1 if temp_ans[4] == a[1] else 0,
        1 if temp_ans[5] == a[0] else 0,
        1 if temp_ans[6] == a[0] else 0,
        1 if temp_ans[7] == a[0] else 0,
        1 if temp_ans[8] == a[0] else 0,
        1 if temp_ans[9] == a[0] else 0,
        1 if temp_ans[10] == a[0] else 0,
        1 if temp_ans[11] == a[1] else 0,
        1 if temp_ans[12] == a[0] else 0,
        1 if temp_ans[13] == a[0] else 0,
        1 if temp_ans[14] == a[1] else 0,
        1 if temp_ans[15] == a[0] else 0,
        1 if temp_ans[16] == a[0] else 0,
        1 if temp_ans[17] == a[1] else 0,
        1 if temp_ans[18] == a[0] else 0,
        1 if temp_ans[19] == a[1] else 0,
        1 if temp_ans[20] == a[0] else 0,
        1 if temp_ans[21] == a[0] else 0,
        1 if temp_ans[22] == a[0] else 0,
        1 if temp_ans[23] == a[0] else 0,
        1 if temp_ans[24] == a[0] else 0,
        1 if temp_ans[25] == a[0] else 0,
        1 if temp_ans[26] == a[0] else 0,
        1 if temp_ans[27] == a[0] else 0,
        1 if temp_ans[28] == a[0] else 0,
        1 if temp_ans[29] == a[1] else 0,
        1 if temp_ans[30] == a[1] else 0,
        1 if temp_ans[31] == a[0] else 0,
        1 if temp_ans[32] == a[1] else 0,
        1 if temp_ans[33] == a[0] else 0,
        1 if temp_ans[34] == a[1] else 0,
        1 if temp_ans[35] == a[0] else 0,
        1 if temp_ans[36] == a[0] else 0,
        1 if temp_ans[37] == a[1] else 0,
        1 if temp_ans[38] == a[0] else 0,
        1 if temp_ans[39] == a[0] else 0,
        1 if temp_ans[40] == a[0] else 0,
        1 if temp_ans[41] == a[0] else 0,
        1 if temp_ans[42] == a[1] else 0,
        1 if temp_ans[43] == a[0] else 0,
        1 if temp_ans[44] == a[0] else 0,
        1 if temp_ans[45] == a[0] else 0,
        1 if temp_ans[46] == a[0] else 0,
        1 if temp_ans[47] == a[0] else 0,
        1 if temp_ans[48] == a[0] else 0,
        1 if temp_ans[49] == a[0] else 0,
        1 if temp_ans[50] == a[0] else 0,
        1 if temp_ans[51] == a[0] else 0,
        1 if temp_ans[52] == a[0] else 0,
        1 if temp_ans[53] == a[0] else 0,
        1 if temp_ans[54] == a[0] else 0,
        1 if temp_ans[55] == a[0] else 0,
        1 if temp_ans[56] == a[0] else 0
    ]
    extraversion = temp_ans[0] + temp_ans[2] + temp_ans[4] + temp_ans[7] + temp_ans[9] + temp_ans[12] + temp_ans[16] + \
                   temp_ans[19] + temp_ans[21] + temp_ans[25] + \
                   temp_ans[27] + temp_ans[29] + temp_ans[32] + temp_ans[34] + temp_ans[37] + temp_ans[39] + \
                   temp_ans[41] + temp_ans[44] + temp_ans[46] + temp_ans[49] + temp_ans[51] + temp_ans[53] + temp_ans[56]
    liar = temp_ans[5] + temp_ans[11] + temp_ans[17] + temp_ans[23] + temp_ans[29] + temp_ans[35] + temp_ans[41] + \
           temp_ans[47] + temp_ans[53]
    neurotism = sum(temp_ans) - extraversion - liar
    if extraversion > 12 and neurotism > 13:
        attempt.temperament = Temperament.objects.get(name='Сангвинник')
    elif extraversion > 12 and neurotism < 9:
        attempt.temperament = Temperament.objects.get(name='Холерик')
    elif extraversion < 12 and neurotism > 13:
        attempt.temperament = Temperament.objects.get(name='Флегматик')
    elif extraversion < 12 and neurotism < 9:
        attempt.temperament = Temperament.objects.get(name='Меланхолик')
    elif extraversion == 12 and neurotism <= 9:
        attempt.temperament = Temperament.objects.get(name='Меланхолик-Холерик')
    elif extraversion == 12 and neurotism >= 13:
        attempt.temperament = Temperament.objects.get(name='Флегматик-Сангвиник')
    elif extraversion >= 12 and 12 <= neurotism <= 19:
        attempt.temperament = Temperament.objects.get(name='Холерик-Сангвинник')
    elif extraversion <= 12 and 9 <= neurotism <= 12:
        attempt.temperament = Temperament.objects.get(name='Меланхолик-Флегматик')
    else:
        attempt.temperament = Temperament.objects.get(name='Неопределенно')
    attempt.save()
    return


def calc_role(attempt, answers):
    role_ans = [ans.answer for ans in answers]
    coordinator = role_ans[3] + role_ans[9] + role_ans[16] + role_ans[31] + role_ans[37] + role_ans[42] + role_ans[54]
    former = role_ans[5] + role_ans[12] + role_ans[18] + role_ans[25] + role_ans[35] + role_ans[46] + role_ans[48]
    generator = role_ans[2] + role_ans[14] + role_ans[19] + role_ans[28] + role_ans[39] + role_ans[40] + role_ans[53]
    expert = role_ans[7] + role_ans[11] + role_ans[22] + role_ans[25] + role_ans[32] + role_ans[44] + role_ans[49]
    worker = role_ans[4] + role_ans[15] + role_ans[17] + role_ans[29] + role_ans[38] + role_ans[43] + role_ans[50]
    researcher = role_ans[0] + role_ans[10] + role_ans[21] + role_ans[30] + role_ans[36] + role_ans[47] + role_ans[51]
    diplomat = role_ans[1] + role_ans[13] + role_ans[20] + role_ans[24] + role_ans[34] + role_ans[41] + role_ans[55]
    realize = role_ans[6] + role_ans[8] + role_ans[23] + role_ans[27] + role_ans[33] + role_ans[45] + role_ans[52]
    maximum = max(coordinator, former, generator, expert, worker, researcher, diplomat, realize)
    if coordinator == maximum:
        attempt.role = 'Председатель / Координатор'
    elif former == maximum:
        attempt.role = 'Творец / Формирователь'
    elif generator == maximum:
        attempt.role = 'Генератор идей / Мыслитель'
    elif expert == maximum:
        attempt.role = 'Эксперт / Оценщик'
    elif worker == maximum:
        attempt.role = 'Работник / Исполнитель'
    elif researcher == maximum:
        attempt.role = 'Исследователь / Разведчик'
    elif diplomat == maximum:
        attempt.role = 'Дипломат / Коллективист'
    elif realize == maximum:
        attempt.role = 'Реализатор / Доводчик'
    else:
        attempt.role = 'Неопределенно'
    attempt.finished = True
    attempt.save()


def main(request):
    if request.method == 'POST':
        username = 'someusername' + str(len(User.objects.all()))
        user = User.objects.create_user(username, username + '@mail.ru', 'somepassword')
        login(request, user)
        user.attempt = Attempt.objects.create(
            name=request.POST['name'],
            grade=request.POST['grade'],
            group=request.POST['group'],
            user=user
        )
        user.save()
        return HttpResponseRedirect('/about_temperament')
    return render(request, 'enter.html')


def about_temperament(request):
    return render(request, 'about_temperament.html')


def temperament_test(request):
    if request.method == 'POST':
        data = {key: request.POST[key] for key in request.POST.keys()}
        for key in data:
            if 'answer' in key:
                fa, _ = FormAnswer.objects.get_or_create(
                    attempt=request.user.attempt,
                    question_id=int(key.split('_')[1])
                )
                fa.answer = data[key]
                fa.save()
        calc_info(request.user.attempt, FormAnswer.objects.filter(attempt=request.user.attempt, question__block__isnull=True))
        return HttpResponseRedirect('/temperament_result')
    return render(request, 'temperament_test.html', {
        'questions': Question.objects.filter(block=None)
    })


def temperament_result(request):
    return render(request, 'temperament_result.html')


def about_role(request):
    return render(request, 'about_role.html')


def role_test(request):
    n = int(request.GET['n'])
    if request.method == 'POST':
        data = {key: request.POST[key] for key in request.POST.keys()}
        for key in data.keys():
            if 'answer' in key:
                fa, _ = FormAnswer.objects.get_or_create(
                    attempt=request.user.attempt,
                    question_id=int(key.split('_')[1])
                )
                fa.answer = data[key]
                fa.save()
        if n != 7:
            return HttpResponseRedirect('/role_test?n=' + str(n + 1))
        else:
            attempt = request.user.attempt
            calc_role(attempt, FormAnswer.objects.filter(attempt=attempt, question__block__isnull=False))
            return HttpResponseRedirect('/end')
    return render(request, 'role_test.html', {
        'questions': Question.objects.filter(block=n),
        'n': n
    })


def end(request):
    return render(request, 'end.html')


@synchronized_method
def plot(request):
    labels = list(request.GET.keys())
    values = [request.GET[label] for label in labels]
    plt.pie(values, labels=labels)
    with open('graph.png', 'wb') as fs:
        plt.savefig(fs, format='png')
    plt.clf()
    response = HttpResponse(open('graph.png', 'rb').read(), content_type='image/png')
    response['Content-Disposition'] = 'inline; filename=img.jpg'
    return response


def results(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    attempts = Attempt.objects.filter(finished=True)
    context = {
        'attempts': attempts,
    }
    graph_data = {}
    groups = list(set([attempt.group for attempt in attempts]))
    for group in groups:
        cur_temps = [attempt.temperament.name for attempt in [a for a in attempts if a.group == group]]
        data = {
            temp: cur_temps.count(temp)
            for temp in set(cur_temps)
        }
        graph_data['Темперамент в группе ' + group] = '?' + '&'.join([f'{temp}={data[temp]}' for temp in cur_temps])
    for group in groups:
        cur_roles = [attempt.role for attempt in [a for a in attempts if a.group == group]]
        data = {
            role: cur_roles.count(role)
            for role in set(cur_roles)
        }
        graph_data['Роли в группе ' + group] = '?' + '&'.join([f'{role}={data[role]}' for role in cur_roles])
    vals = [str((att.temperament, att.role)) for att in attempts]
    keys = set(vals)
    graph_data['Общая статистика'] = '?' + '&'.join([f'{val}={vals.count(val)}' for val in keys])
    context['graph_data'] = graph_data
    return render(request, 'results.html', context)
