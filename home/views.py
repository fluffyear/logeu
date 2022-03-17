from django.shortcuts import render
from home.RanP import funx as funx
from home.RanP import RandomNoun as ranoun
import random


def index(request):
    return render(request, 'index.html')


def verbs(request):
    count = 1
    context = {}
    dct = {}
    while count < 6:
        val = funx.type_get_pp(1)
        if val in dct.values():
            continue
        dct['word' + str(count)] = val
        count += 1
    choix = random.choice(list(dct.keys()))
    context['ans_greek'] = dct[choix][0]
    context['ans_word'] = dct[choix][1]
    for num, value in enumerate(dct.values(), start=1):
        context['word' + str(num)] = value[0]
    return render(request, 'verbs.html', context)


def nouns(request):
    context = {}
    imp = ranoun.rand_all()
    rest = ranoun.rand_exc_case(imp[0])
    lst = []
    for k in rest:
        lst.append(k)
    lst.append(imp[0])
    random.shuffle(lst)
    for num, value in enumerate(lst, start=1):
        context['word' + str(num)] = value
    context['ans_word'] = imp[1]
    context['ans_case'] = imp[0]
    return render(request, 'nouns.html', context)
