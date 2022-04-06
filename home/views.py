from django.shortcuts import render
import random
from unicodedata import normalize as norm
from home.RanP import funx
from home.RanP import RandomNoun as RaNoun
from home.RanP import as_vocab_func as asv
word_key = {"θ": "th", "ξ": "ks", "φ": "ph", "ψ": "ps", "Ἑ": "\'E", "ἱ": "\'i", "ὑ": "\'u", "ἡ": "\'n", "ῥ": "\'r",
            "ᾳ": "a!", "ῃ": "n!"}
key_lst1 = ['α', 'ἁ', 'ᾳ', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ']
key_lst2 = ['a', '\'a', 'a!', 'b', 'g', 'd', 'e', 'z', 'n', 'th', 'i', 'k', 'l']
key_lst3 = ['μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
key_lst4 = ['m', 'v', 'ks', 'o', 'p', 'r', 's', 't', 'u', 'ph', 'x', 'ps', 'w']
up_key_lst1 = ['Α', 'Ἁ', 'ᾼ', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ']
up_key_lst2 = ['A', '\'A', 'A!', 'B', 'G', 'D', 'E', 'Z', 'N', 'TH', 'I', 'K', 'L']
up_key_lst3 = ['Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
up_key_lst4 = ['M', 'V', 'KS', 'O', 'P', 'R', 'S', 'T', 'U', 'PH', 'X', 'PS', 'W']
unicode_exclusion = {
    ord('\u0300'): None,
    ord('\u0301'): None,
    ord('\u0302'): None,
    ord('\u0303'): None,
    ord('\u0304'): None,
    ord('\u0305'): None,
    ord('\u0306'): None,
    ord('\u0307'): None,
    ord('\u0308'): None,
    ord('\u0309'): None,
    ord('\u030a'): None,
    ord('\u030b'): None,
    ord('\u030c'): None,
    ord('\u030d'): None,
    ord('\u030e'): None,
    ord('\u030f'): None,
    ord('\u0310'): None,
    ord('\u0311'): None,
    ord('\u0313'): None,
    ord('\u0340'): None,
    ord('\u0341'): None,
    ord('\u0342'): None,
    ord('\u0343'): None,
    ord('\u0344'): None,
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
    lst = RaNoun.rand_exc_case(imp) + [imp[0]]
    random.shuffle(lst)
    for num, value in enumerate(lst, start=1):
        context['word' + str(num)] = value
    context['ans_word'] = imp[1]
    context['ans_case'] = imp[0]
    context['ans_base'] = imp[4] + imp[2][1]
    context['num_case'] = imp[3]
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
    imp = RaNoun.rand_all()
    print(imp)
    ans_eng = ""
    context = {'ans_word': imp[1],
               'ans_case': imp[0],
               'num_case': imp[3],
               'key_lst1': key_lst1,
               'key_lst2': key_lst2,
               'key_lst3': key_lst3,
               'key_lst4': key_lst4,
               'up_key_lst1': up_key_lst1,
               'up_key_lst2': up_key_lst2,
               'up_key_lst3': up_key_lst3,
               'up_key_lst4': up_key_lst4
               }
    for num, value in enumerate(list(imp[2].values()), start=1):
        context['table' + str(num)] = imp[4] + value
    if imp[3] == 1:
        context['ans_base'] = context['table' + str(random.randint(2, 8))]
    else:
        context['ans_base'] = imp[4] + imp[2][1]
    for i in imp[1].translate(imp[1].maketrans("αἀβγδεἐζηἠιἰκλμνοὀπρσςτυχω", "aabgdeeznniiklmvooprsstuxw")):
        if i in set(word_key):
            ans_eng += word_key[i]
        else:
            ans_eng += i
    context['ans_simp1'] = imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥᾳῃ", "αΕειιουηηραη"))
    context['ans_simp2'] = imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥ", "αΕειιουηηρ"))
    context['ans_simp3'] = imp[1].translate(imp[1].maketrans("ᾳῃ", "αη"))
    context['ans_eng'] = ans_eng
    return render(request, 'noun_input.html', context)


def gre_vocab_input(request):
    ch = asv.gre_word()
    context = {
        'ans_greek': ch[0],
        'ans_word': ch[1],
        'ans_word_list': ch[1].split(", ")
    }
    return render(request, 'gre_vocab_input.html', context)


def eng_vocab_input(request):
    ch = asv.gre_word()
    ans_greek = norm('NFD', ch[0]).translate(unicode_exclusion)
    ans_eng = ""
    context = {'ans_greek': ans_greek,
               'ans_greek_full': ch[0],
               'ans_word': ch[1],
               'ans_word_shaven': asv.shave(ch[1]),
               'letter1': ch[0][0],
               'key_lst1': key_lst1,
               'key_lst2': key_lst2,
               'key_lst3': key_lst3,
               'key_lst4': key_lst4,
               'up_key_lst1': up_key_lst1,
               'up_key_lst2': up_key_lst2,
               'up_key_lst3': up_key_lst3,
               'up_key_lst4': up_key_lst4
               }
    ag_simple = norm('NFD', ans_greek).translate(
        {'\u0314': None, '\u0345': None}).replace("\u0314", "").replace("\u0345", "")
    diphthong = {"θ": "th", "ξ": "ks", "φ": "ph", "ψ": "ps"}
    for i in ag_simple.translate(ag_simple.maketrans("αβγδεζηικλμνοπρσςτυχω", "abgdezniklmvoprsstuxw")):
        if i in set(diphthong):
            ans_eng += diphthong[i]
        else:
            ans_eng += i
    context['ans_simp1'] = norm('NFD', ans_greek).translate(
        {'\u0314': None, '\u0345': None}).replace("\u0314", "").replace("\u0345", "")
    context['ans_simp2'] = norm('NFD', ans_greek).translate({'\u0314': None}).replace("\u0314", "")
    context['ans_simp3'] = norm('NFD', ans_greek).translate({'\u0345': None}).replace("\u0345", "")
    context['ans_eng'] = ans_eng
    context['ans_simp_plus'] = ''
    return render(request, 'eng_vocab_input.html', context)
