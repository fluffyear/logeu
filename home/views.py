from django.shortcuts import render
from home.RanP import funx
from home.RanP import RandomNoun as RaNoun
from home.RanP import as_vocab_func as asv
import random
word_key = {
    "θ": "th",
    "ξ": "ks",
    "φ": "ph",
    "ψ": "ps",
    "Ἑ": "\'E",
    "ἱ": "\'i",
    "ὑ": "\'u",
    "ἡ": "\'n",
    "ῥ": "\'r",
    "ᾳ": "a!",
    "ῃ": "n!"
}


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


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
    context['ans_base'] = imp[4] + imp[2][1]
    for num, value in enumerate(list(imp[2].values()), start=1):
        context['table' + str(num)] = imp[4] + value
    return render(request, 'nouns.html', context)


def gre_vocab(request):
    ch = asv.gre_selection()
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
    return render(request, 'vocab_greek.html', context)


def eng_vocab(request):
    ch = asv.eng_selection()
    words = [asv.choose(asv.shave(ch[0][0])), ch[1], ch[2], ch[3], ch[4]]
    random.shuffle(words)
    context = {
        'word1': words[0],
        'word2': words[1],
        'word3': words[2],
        'word4': words[3],
        'word5': words[4],
        'ans_greek': ch[0][0],
        'ans_word': ch[0][1]
    }
    return render(request, 'vocab_english.html', context)


def noun_input(request):
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
    context['ans_base'] = imp[4] + imp[2][1]
    proto_eng = imp[1].translate(imp[1].maketrans("αἀβγδεἐζηἠιἰκλμνοὀπρσςτυχω", "aabgdeeznniiklmvooprsstuxw"))
    ans_eng = ""
    for i in proto_eng:
        if i in set(word_key):
            ans_eng += word_key[i]
        else:
            ans_eng += i
    simp1 = imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥᾳῃ", "αΕειιουηηραη"))
    simp2 = imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥ", "αΕειιουηηρ"))
    simp3 = imp[1].translate(imp[1].maketrans("ᾳῃ", "αη"))
    context['ans_simp1'] = simp1
    context['ans_simp2'] = simp2
    context['ans_simp3'] = simp3
    context['ans_eng'] = ans_eng
    for num, value in enumerate(list(imp[2].values()), start=1):
        context['table' + str(num)] = imp[4] + value
    return render(request, 'noun_input.html', context)
