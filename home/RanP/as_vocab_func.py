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


def gre_selection():  # this is broken now
    key = list(dct.keys())
    num = rn.randint(0, len(key)-1)
    ans = key[num]
    verb = ans[0] == 'I'
    ans_tup = (choose(ans), dct[ans])
    if num < 6:
        rain = g_lst[:13]  # rain = range over which to pick words
    elif num > len(key) - 7:
        rain = g_lst[len(key) - 12:]
    else:
        rain = g_lst[num - 6:num + 7]
    rain.remove(ans)
    v_pick = []
    nv_pick = []
    for item in rain:
        if len(v_pick) < 2 and item[0] == 'I':
            v_pick.append(item)
            rain.remove(item)
            continue
        if len(nv_pick) < 2 and item[0] != 'I':
            nv_pick.append(item)
            rain.remove(item)
            continue
        break
    if verb:
        temp = v_pick
    else:
        temp = nv_pick
    while len(temp) < 4:
        poss = rn.choice(key)
        if poss in set(temp) and (poss[0] == 'I') != verb:
            continue
        temp.append(poss)
    temp.append(rain.pop(rn.randint(0, len(rain) - 1)))
    rn.shuffle(temp)
    return ans_tup, shave(dct[temp[0]]), shave(dct[temp[1]]), shave(dct[temp[2]]), shave(dct[temp[3]])


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


gre_selection()
