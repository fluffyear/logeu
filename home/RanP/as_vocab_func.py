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


def shave(word):  # shave definition to max 2 parts
    lst = word.split(', ')
    if len(lst) < 3:
        return word
    return f"{lst[0]}, {lst[1]}"


def gre_selection():
    key = list(dct.keys())
    ans = rn.choice(key)
    verb = dct[ans][0] == 'I'
    ans_tup = (choose(ans), shave(dct[ans]))
    ind = g_lst.index(ans)
    alpha = g_lst[ind-7:ind+7]
    if not alpha:
        if ind < 7:
            alpha = g_lst[:15-ind]
        else:
            alpha = g_lst[len(key)-15+ind:]
    else:
        alpha.pop(7)
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
    cho4 = rn.choice(verbs+non_verbs)
    return ans_tup, shave(dct[cho1]), shave(dct[cho2]), shave(dct[cho3]), shave(dct[cho4])


def eng_selection():
    key = list(dct.keys())
    num = rn.randint(0, len(key)-1)
    ans = key.pop(num)
    ans_tup = (ans, dct[ans])
    verb = ans[0] == 'I'
    temp = []
    for _ in range(6):
        ind = rn.randint(0, len(key)-1)
        if (key[ind][0] == 'I') != verb:
            continue
        temp.append(key.pop(ind))
    if num < 6:
        rain = key[:12+num]  # rain = range over which to pick words
    elif num > len(key)-6:
        rain = key[len(key)-12-num:]
    else:
        rain = key[num-6:num+5]
    rn.shuffle(rain)
    v_pick = ''
    nv_pick = ''
    for item in rain:
        if not v_pick and item[0] == 'I':
            v_pick = item
            continue
        if not nv_pick and item[0] != 'I':
            nv_pick = item
            continue
        break
    temp.append(v_pick) if verb else temp.append(nv_pick)
    len_r = len(rain)-1
    temp.append(rain.pop(rn.randint(0, len_r)))
    rn.shuffle(temp)
    return ans_tup, choose(temp[0]), choose(temp[1]), choose(temp[2]), choose(temp[3])
