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
with open(os.path.join(__location__, 'vendings.txt'), encoding='utf8') as f_hand:
    names = list(order)
    temp_list = []
    dct1 = {}
    probs = []
    for line in f_hand:
        if line in {"", "\n", " "}:
            dct1[names.pop(0)] = temp_list
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
            dct2[names.pop(0)] = temp_list
            temp_list = []
        else:
            temp_list.append(line.rstrip(" \n"))


def ran():
    cho = rn.choice(list(dct1.keys()))
    ind = rn.randint(0, len(dct1[cho]) - 1)
    return cho[ind], cho, ind


def ran_luo():
    cho = rn.choices(list(dct1.keys()), probs)[0]
    ind = rn.randint(0, len(dct1[cho]) - 1)
    ans = ""
    for c in cho.split(" "):
        ans += str(code[c]) + ","
    ans += str(ind)
    full = ""
    for c in cho.split(" "):
        full += f"{code1[c]} "
    return f"{dct2[cho][ind]}{dct1[cho][ind]}", cho, ind, ans, len(dct1[cho]), full, \
        [f"{dct2[cho][i]}{dct1[cho][i]}" for i in range(0, len(dct1[cho]))]
