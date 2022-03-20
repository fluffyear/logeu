from django.shortcuts import render
from home.RanP import funx as funx
from home.RanP import RandomNoun as RaNoun
from home.RanP import as_vocab_func as asv
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
    imp = RaNoun.rand_all()
    rest = RaNoun.rand_exc_case(imp)
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


def vocab(request):
    ch = asv.selection()
    words = [asv.shave(ch[0][1]), ch[1], ch[2], ch[3], ch[4]]
    random.shuffle(words)
    context = {
        'word1': words[0],
        'word2': words[1],
        'word3': words[2],
        'word4': words[3],
        'word5': words[4],
        'ans_greek': ch[0][1],
        'ans_word': ch[0][0]
    }
    return render(request, 'vocab.html', context)
