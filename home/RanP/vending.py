import random as rn
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
order = [
    'act pre ind',
    'act pre sub',
    'act pre opt',
    'act pre imp',
    'act pre inf',
    'act pre par',
    'act ipf ind',
    'act fut ind',
    'act fut opt',
    'act fut inf',
    'act fut par',
    'act aor ind',
    'act aor sub',
    'act aor opt',
    'act aor imp',
    'act aor inf',
    'act aor par',
    'act per ind',
    'act per sub',
    'act per opt',
    'act per inf',
    'act per par',
    'act plu ind',
    'mid pre ind',
    'mid pre sub',
    'mid pre opt',
    'mid pre imp',
    'mid pre inf',
    'mid pre par',
    'mid ipf ind',
    'mid fut ind',
    'mid fut opt',
    'mid fut inf',
    'mid fut par',
    'mid aor ind',
    'mid aor sub',
    'mid aor opt',
    'mid aor imp',
    'mid aor inf',
    'mid aor par',
    'mid per ind',
    'mid per sub',
    'mid per opt',
    'mid per imp',
    'mid per inf',
    'mid per par',
    'mid plu ind',
    'pas pre ind',
    'pas pre sub',
    'pas pre opt',
    'pas pre imp',
    'pas pre inf',
    'pas pre par',
    'pas ipf ind',
    'pas fut ind',
    'pas fut opt',
    'pas fut inf',
    'pas fut par',
    'pas aor ind',
    'pas aor sub',
    'pas aor opt',
    'pas aor imp',
    'pas aor inf',
    'pas aor par',
    'pas per ind',
    'pas per sub',
    'pas per opt',
    'pas per inf',
    'pas per par',
    'pas plu ind'
]
code = {
    "act": 0,
    "mid": 1,
    "pas": 2,
    "ind": 0,
    "sub": 1,
    "opt": 2,
    "imp": 3,
    "inf": 4,
    "par": 5,
    "pre": 0,
    "fut": 1,
    "ipf": 2,
    "aor": 3,
    "per": 4,
    "plu": 5,
}
code1 = {
    "act": "Active",
    "mid": "Middle",
    "pas": "Passive",
    "ind": "Indicative",
    "sub": "Subjunctive",
    "opt": "Optative",
    "imp": "Imperative",
    "inf": "Infinitive",
    "par": "Participle",
    "pre": "Present",
    "fut": "Future",
    "ipf": "Imperfect",
    "aor": "Aorist",
    "per": "Perfect",
    "plu": "Pluperfect",
}
re = {0: "λυ", 1: "λύ"}
map1 = {1: "1sg", 2: "2sg", 3: "3sg", 4: "1pl", 5: "2pl", 6: "3pl"}
map2 = {1: "2sg", 2: "3sg", 3: "2pl", 4: "3pl"}
map3 = {1: "masc", 2: "fem", 3: "neut"}
map4 = {1: ""}
map_map = {6: map1, 4: map2, 3: map3, 1: map4}
with open(os.path.join(__location__, 'vendings.txt'), encoding='utf8') as f_hand:
    names = list(order)
    temp_list = []
    dct1 = {}
    word_dct = {}
    probs = []
    for line in f_hand:
        if line in {"", "\n", " "}:
            temp_name = names.pop(0)
            dct1[temp_name] = temp_list
            word_dct[temp_name] = temp_list
            probs.append(len(temp_list))
            temp_list = []
        else:
            temp_list.append(line.rstrip(" \n"))
with open(os.path.join(__location__, 'vprefixes.txt'), encoding='utf8') as f_hand:
    names = list(order)
    temp_list = []
    dct2 = {}
    for line in f_hand:
        if line in {"", "\n", " "}:
            temp_name = names.pop(0)
            dct2[temp_name] = temp_list
            for count, val in enumerate(temp_list):
                before = word_dct[temp_name][count]
                word_dct[temp_name][count] = val
                word_dct[temp_name][count] += before
            temp_list = []
        else:
            temp_list.append(line.rstrip(" \n"))
with open(os.path.join(__location__, 'tithnmi.txt'), encoding='utf8') as f_hand:
    names = list(order)
    temp_list = []
    t_word_dct = {}
    for line in f_hand:
        if line in {"", "\n", " "}:
            temp_name = names.pop(0)
            t_word_dct[temp_name] = temp_list
            temp_list = []
        else:
            temp_list.append(line.rstrip(" \n"))
lzt_map = {"tithnmi": t_word_dct, "luw": word_dct}


def ran():
    cho = rn.choice(list(dct1.keys()))
    ind = rn.randint(0, len(dct1[cho]) - 1)
    return cho[ind], cho, ind


def ran_luo(lzt=None):
    if lzt is not None:
        lzt_t = [i for i in lzt if i != "false"]
        if len(lzt_t) in {0, 2}:
            dct = rn.choice([word_dct, t_word_dct])
        else:
            if lzt[1] == "true":
                dct = lzt_map["luw"]
            else:
                dct = lzt_map["tithnmi"]
    else:
        dct = rn.choice([word_dct, t_word_dct])
    cho = rn.choices(order, probs)[0]
    ind = rn.randint(0, len(dct[cho]) - 1)
    ans = ""
    for c in cho.split(" "):
        ans += str(code[c]) + ","
    ans += str(ind)
    full = ""
    for c in cho.split(" "):
        full += f"{code1[c]} "
    word = dct[cho][ind]
    nots = []
    for tag, lst in list(dct.items()):
        for c, i in enumerate(lst):
            if i == word and tag != cho:
                t = tag.split(" ")
                held = t[0]
                t[0] = t[1]
                t[1] = held
                held = t[1]
                t[1] = t[2]
                t[2] = held
                t1 = ""
                for counter, item in enumerate(t, start=1):
                    t1 += item
                    if counter != len(t):
                        t1 += " "
                t2 = map_map[len(lst)][c+1]
                nots.append(f"{t1} {t2}")
    t = full.split(" ")
    held = t[0]
    t[0] = t[1]
    t[1] = held
    held = t[1]
    t[1] = t[2]
    t[2] = held
    v5 = ""
    for counter, item in enumerate(t, start=1):
        v5 += item
        if counter != len(t):
            v5 += " "
    return word, cho, ind, ans, len(dct[cho]), v5, \
        [dct[cho][i] for i in range(0, len(dct[cho]))], nots
