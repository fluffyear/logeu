import random
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, "pp.txt"), encoding="utf8") as f_hand:
    count1 = 0
    lst = []
    temp = []
    for line in f_hand:
        if count1 % 2 == 0:
            line = line.split(",")[:-1] + [line.split(",")[-1].strip()]
            temp += line
        else:
            temp.append(line.strip())
            lst += [tuple(temp)]
            temp = []
        count1 += 1


def fin(ind, el):  # Condensing repeated indexing
    return el[ind][:el[ind].find(".") + 1]


dct = {}
for elem in lst:  # Constructing dictionary to have keys containing any keywords in value
    if elem[-2].find(".") > -1:
        if elem[-3].find(".") > -1:
            if elem[-4].find(".") > -1:
                dct[(elem[-1], (fin(-2, elem), fin(-3, elem), fin(-4, elem)))] = elem[:-1]
            else:
                dct[(elem[-1], (fin(-2, elem), fin(-3, elem)))] = elem[:-1]
        else:
            dct[(elem[-1], fin(-2, elem))] = elem[:-1]
    else:
        dct[elem[-1]] = elem[:-1]


def choose(pp):
    return random.choice(pp.split("/")).strip()


def remove_crud(contents):
    if isinstance(contents, tuple):
        return contents[0]
    return contents


def get_pp(key_, type_):  # type_ is int 1 to 6, or a "principal p. keyword"
    verb = dct.get(key_)
    if isinstance(type_, int):
        try:
            if isinstance(verb[int(type_) - 1], str):
                return choose(verb[int(type_) - 1]), key_, type_
            elif isinstance(verb[int(type_) - 1], tuple):
                return choose(verb[int(type_) - 1][0]), key_[0], type_
        except IndexError:
            return "-"
    elif type_.find(".") is True:
        try:
            return choose(verb[type_][type_.index(type_)+len(type_):]), key_, type_
        except IndexError:
            return "-"
    else:
        return "-"


def type_get_pp(type_):
    while True:
        if isinstance(type_, int):
            verb = random.choice(list(dct))
            try:
                part = dct[verb][type_-1]
                if part != "-" and isinstance(part, str):
                    return choose(part), remove_crud(verb), type_
                elif part != "-" and isinstance(part, tuple):
                    return choose(part[0]), remove_crud(verb[0]), type_
                else:
                    continue
            except IndexError:
                continue
        elif type_.find(".") > -1:
            try:
                vals = []
                count2 = 0
                keys = list(dct)
                for key in keys:
                    try:
                        if isinstance(key, tuple):
                            vals += [count2]
                        count2 += 1
                    except ValueError:
                        count2 += 1
                f_key = keys[random.choice(vals)]
                verb = dct.get(f_key)
                count3 = 0
                for v in verb:
                    if v.find(type_) > -1:
                        return choose(verb[count3]), remove_crud(f_key[0]), type_
                    count3 += 1
            except IndexError:
                continue
        else:
            return "-"


def rand_pp():
    key = random.choice(list(dct))
    verb = dct.get(key)
    while True:
        num = random.randint(0, len(verb)-1)
        typ = verb[num]
        if typ == "-":
            continue
        elif isinstance(key, str):
            return choose(typ), remove_crud(key), num+1
        elif typ.find(".") == -1 and key[-1].find(".") > -1:
            return choose(typ), remove_crud(key[0]), num+1
        else:
            return choose(typ), remove_crud(key[0]), typ[:typ.find(".")+1]
