import random as rn
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'as_vocab.txt'), encoding='utf8') as f_hand:
    greek = True
    dct = {}
    g_lst = []
    e_lst = []
    for line in f_hand:
        if line == '\n':
            greek = not greek
            continue
        line = line.rstrip('\n')
        g_lst.append(line) if greek else e_lst.append(line)
    dct = dict(zip(g_lst, e_lst))


def choose(word):
    if word.find(',') != -1:
        return rn.choice(word.split(', '))
    return word


def shave(word):
    lst = word.split(', ')
    if len(lst) < 3:
        return word
    return f"{lst[0]}, {lst[1]}"


def selection():
    key = list(dct.keys())
    ans = rn.choice(key)
    verb = dct[ans][0] == 'I'
    ans_tup = (choose(ans), shave(dct[ans]))
    ind = g_lst.index(ans)
    alpha = g_lst[ind-6:ind+6]
    if not alpha:
        if ind < 6:
            alpha = g_lst[:13-ind]
        else:
            alpha = g_lst[752+ind:]
    else:
        alpha.pop(6)
    non_verbs = []
    verbs = []
    for i in alpha:
        if i[0] != 'I':
            non_verbs.append(i)
        else:
            verbs.append(i)
    if verb:
        alpha = verbs
    else:
        alpha = non_verbs
    if not alpha:
        cho1 = rn.choice(key)
        cho2 = rn.choice(key)
        cho3 = rn.choice(key)
    elif len(alpha) == 1:
        cho1 = alpha[0]
        cho2 = rn.choice(key)
        cho3 = rn.choice(key)
    elif len(alpha) == 2:
        cho1 = alpha[0]
        cho2 = alpha[1]
        cho3 = rn.choice(key)
    else:
        cho1 = rn.choice(alpha)
        alpha.remove(cho1)
        cho2 = rn.choice(alpha)
        alpha.remove(cho2)
        cho3 = rn.choice(alpha)
        alpha.remove(cho3)
    cho4 = rn.choice(list(set(dct.keys()) - {ans, cho1, cho2, cho3}))
    return ans_tup, shave(dct[cho1]), shave(dct[cho2]), shave(dct[cho3]), shave(dct[cho4])
