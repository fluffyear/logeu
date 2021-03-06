from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import random
from unicodedata import normalize as norm
from home.RanP import funx, RandomNoun as RaNoun, as_vocab_func as asv, logeupmf as pmfs, vending as ven
import json
word_key = {"θ": "th", "ξ": "ks", "φ": "ph", "ψ": "ps", "Ἑ": "\'E", "ἱ": "\'i", "ὑ": "\'u", "ἡ": "\'n", "ῥ": "\'r",
            "ᾳ": "a!", "ῃ": "n!"}
key_lst1 = ['α', 'ἁ', 'ᾳ', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ']
alt_key_lst1 = ['α', 'ἁ', 'ᾳ', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ']
key_lst2 = ['a', '\'a', 'a!', 'b', 'g', 'd', 'e', 'z', 'n', 'th', 'i', 'k', 'l']
key_lst3 = ['μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
key_lst4 = ['m', 'v', 'ks', 'o', 'p', 'r', 's', 't', 'u', 'ph', 'x', 'ps', 'w']
up_key_lst1 = ['Α', 'Ἁ', 'ᾼ', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ']
alt_up_key_lst1 = ['Α', 'Ἁ', 'ᾼ', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ']
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


def verb_endings_settings(request):
    return render(request, 'verb_endings_settings.html')


def context_verb():
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
    return context


def verbs(request):
    return render(request, 'verbs.html', context_verb())


def context_noun():
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
    return context


def nouns(request):
    return render(request, 'nouns.html', context_noun())


def context_gre_vocab():
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
    return context


def gre_vocab(request):
    return render(request, 'vocab_greek.html', context_gre_vocab())


def context_eng_vocab():
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
    return context


def eng_vocab(request):
    return render(request, 'vocab_english.html', context_eng_vocab())


def context_noun_input():
    imp = RaNoun.rand_all()
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
    context['members_list'] = (
        f'{imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥᾳῃ", "αΕειιουηηραη"))},'
        f'{imp[1].translate(imp[1].maketrans("ἀἙἐἱἰὀὑἡἠῥ", "αΕειιουηηρ"))},'
        f'{imp[1].translate(imp[1].maketrans("ᾳῃ", "αη"))},'
        f'{imp[1]}'
    )
    print(context['members_list'])
    context['ans_eng'] = ans_eng
    return context


def noun_input(request):
    return render(request, 'noun_input.html', context_noun_input())


def context_gre_vocab_input(obj=None, cho=None, exc=None):
    if obj is None:
        ch = asv.gre_word()
        length = asv.get_len()
        v_list = [1]*length
        f_list = [0]*length
    else:
        ch = asv.gre_word(cho, exc)
        v_list = obj.rights
        f_list = obj.wrongs
    ans_word_list = ""
    ch1_lst = ch[1].split(",")
    for num, i in enumerate(ch1_lst, start=1):
        ans_word_list += f"{i},"
        if num == len(ch1_lst):
            ans_word_list = ans_word_list[:-1]
    context = {
        'ans_greek': ch[0],
        'ans_word': ch[1],
        'ans_full': ch[2],
        'ans_word_list': ans_word_list,
        'v_list': v_list,
        'f_list': f_list,
        'cache': None
    }
    return context


def gre_vocab_input(request):
    return render(request, 'gre_vocab_input.html', context_gre_vocab_input())


def context_eng_vocab_input():
    ch = asv.gre_word()
    ans_greek = norm('NFD', ch[0]).translate(unicode_exclusion)
    ans_eng = ""
    context = {'ans_greek_full': ch[0],
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
    s1a = norm('NFD', ans_greek).translate({'\u0314': None, '\u0345': None}).replace("\u0314", "").replace("\u0345", "")
    s2a = norm('NFD', ans_greek).translate({'\u0314': None}).replace("\u0314", "")
    s3a = norm('NFD', ans_greek).translate({'\u0345': None}).replace("\u0345", "")
    s1b = norm('NFC', s1a)
    s2b = norm('NFC', s2a)
    s3b = norm('NFC', s3a)
    context['ans_eng'] = ans_eng
    context['ans_simp_plus'] = ''
    context['members_list'] = f"{s1a},{s2a},{s3a},{s1b},{s2b},{s3b},{ans_greek},{ch[0]}"
    return context


def eng_vocab_input(request):
    return render(request, 'eng_vocab_input.html', context_eng_vocab_input())


def context_verb_endings(lst=None):
    if lst is not None:
        vending = ven.ran_luo(lst)
    else:
        vending = ven.ran_luo()
    temp = vending[3]
    ans_code = f"{temp[0]},{temp[2]},{temp[4]},{temp[6]}"
    context = {
        "ans_eng": vending[1],
        "ans_greek": vending[0],
        "ans_num": vending[2],
        "ans_code": ans_code,
        "ans_len": vending[4],
        "ans_full": vending[5],
        "table": vending[6],
        "py_nots": vending[7],
        "tier1": ["Act", "Mid", "Pass"],
        "tier2": ["Pres", "Fut", "Ipf", "Aor", "Per", "Plu"],
        "tier3": ["Ind", "Sub", "Opt", "Imp", "Inf", "Part"]
    }
    if vending[4] == 4:
        table = vending[6]
        table.insert(0, "-")
        table.insert(3, "-")
        context['table'] = table
        context["tier4"] = ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"]
    elif vending[4] > 3:
        context["tier4"] = ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"]
    elif vending[4] == 3:
        context["tier4"] = ["Masc", "Fem", "Neut"]
    elif vending[4] == 1:
        context["tier4"] = []
    return context


def verb_endings(request):
    return render(request, 'verb_endings.html', context_verb_endings())


def update_noun(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_noun().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_verb(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_verb().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_gre_vocab_input(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        dct = dict(json.load(request))
        greek_lst = asv.get_greek()
        ind = greek_lst.index(dct["ans_full"])
        pmf = pmfs.Pmf(greek_lst, dct["v_list"], dct["f_list"])
        pmf.cache = dct['cache']
        # cache still not fully working
        pmf.update(ind, dct["data"])
        context = context_gre_vocab_input(pmf, pmf.choose_norm(), pmf.cache)
        context['cache'] = ind
        return JsonResponse({'context': list(context.items())})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_eng_vocab(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_eng_vocab().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_noun_input(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_noun_input().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_eng_vocab_input(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_eng_vocab_input().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_gre_vocab(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_gre_vocab().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def update_verb_endings(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        context_data = list(context_verb_endings().items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')


def post_update_verb_endings(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        dct = dict(json.load(request))
        context_data = list(context_verb_endings([dct["tithnmi"], dct["luw"]]).items())
        return JsonResponse({'context': context_data})
    else:
        return HttpResponseBadRequest('Invalid request')
