from random import randint, choice
corr = {
    1: "nominative singular",
    2: "accusative singular",
    3: "genitive singular",
    4: "dative singular",
    5: "nominative plural",
    6: "accusative plural",
    7: "genitive plural",
    8: "dative plural"
}
n1_fwvn = ("φωνη", "κεφαλη", "ἡδονη", "εἰρηνη")
n1_tolma = ("τολμα", "θαλασσα")
n1_xwra = ("χωρα", "ἀπορια")
n1_vautns = ("ναυτης", "πολιτης")
n1_veavias = ("νεανιας",)
n2_logos = ("λογος", "ἱππος", "ἀνθροπος")
n2_dwrov = ("δωρον", "ζυγον", "ἐργον")
n2_vous = ("νους", "πλους")
n2_ostouv = ("ὀστουν",)
n2_vews = ("νεως",)
n3_limnv = ("λιμην",)
n3_fulaks = ("φυλαξ",)
n3_swma = ("σωμα", "πραγμα")
n3_gerwv = ("γερων")
d1_fwvn = {1: "η", 2: "ην", 3: "ης", 4: "ῃ", 5: "αι", 6: "ας", 7: "ων", 8: "αις"}
d1_tolma = {1: "α", 2: "αν", 3: "ης", 4: "ῃ", 5: "αι", 6: "ας", 7: "ων", 8: "αις"}
d1_xwra = {1: "α", 2: "αν", 3: "ας", 4: "ᾳ", 5: "αι", 6: "ας", 7: "ων", 8: "αις"}
d1_vautns = {1: "ης", 2: "ην", 3: "ου", 4: "ῃ", 5: "αι", 6: "ας", 7: "ων", 8: "αις"}
d1_veavias = {1: "ας", 2: "αν", 3: "ου", 4: "ᾳ", 5: "αι", 6: "ας", 7: "ων", 8: "αις"}
d2_logos = {1: "ος", 2: "ον", 3: "ου", 4: "ῳ", 5: "οι", 6: "ους", 7: "ων", 8: "οις"}
d2_dwrov = {1: "ον", 2: "ον", 3: "ου", 4: "ῳ", 5: "α", 6: "α", 7: "ων", 8: "οις"}
d2_vous = {1: "ους", 2: "ουν", 3: "ου", 4: "ῳ", 5: "οι", 6: "ους", 7: "ων", 8: "οις"}
d2_ostouv = {1: "ουν", 2: "ουν", 3: "ου", 4: "ῳ", 5: "α", 6: "α", 7: "ων", 8: "οις"}
d2_vews = {1: "ως", 2: "ων", 3: "ω", 4: "ῳ", 5: "ῳ", 6: "ως", 7: "ων", 8: "ῳς"}
d3_limnv = {1: "ην", 2: "ενα", 3: "ενος", 4: "ενι", 5: "ενες", 6: "ενας", 7: "ενων", 8: "εσι(ν)"}
d3_fulaks = {1: "αξ", 2: "ακα", 3: "ακος", 4: "ακι", 5: "ακες", 6: "ακας", 7: "ακων", 8: "αξι(ν)"}
d3_swma = {1: "α", 2: "α", 3: "ατος", 4: "ατι", 5: "ατα", 6: "ατα", 7: "ατων", 8: "ασι(ν)"}
d3_gerwv = {1: "ων", 2: "οντα", 3: "οντος", 4: "οντι", 5: "οντες", 6: "οντας", 7: "οντων", 8: "ουσι(ν)"}
dct1 = {
    n1_fwvn: d1_fwvn,
    n1_tolma: d1_tolma,
    n1_xwra: d1_xwra,
    n1_vautns: d1_vautns,
    n1_veavias: d1_veavias
}
dct2 = {
    n2_logos: d2_logos,
    n2_dwrov: d2_dwrov,
    n2_vous: d2_vous,
    n2_ostouv: d2_ostouv,
    n2_vews: d2_vews
}
dct3 = {
    n3_limnv: d3_limnv,
    n3_fulaks: d3_fulaks,
    n3_swma: d3_swma,
    n3_gerwv: d3_gerwv
}
dct_all = {
    n1_fwvn: d1_fwvn,
    n1_tolma: d1_tolma,
    n1_xwra: d1_xwra,
    n1_vautns: d1_vautns,
    n1_veavias: d1_veavias,
    n2_logos: d2_logos,
    n2_dwrov: d2_dwrov,
    n2_vous: d2_vous,
    n2_ostouv: d2_ostouv,
    n2_vews: d2_vews,
    n3_limnv: d3_limnv,
    n3_fulaks: d3_fulaks,
    n3_swma: d3_swma,
    n3_gerwv: d3_gerwv
}


def rand_all():
    n_type = choice(list(dct_all.keys()))
    part = randint(1, 8)
    di = dct_all.get(n_type)
    if n_type in [n3_swma, n1_fwvn, n1_tolma, n1_xwra]:
        return corr[part], n_type[randint(0, len(n_type)-1)][:-1] + di.get(part), di, part
    elif n_type in [n2_vous, n2_ostouv]:
        return corr[part], n_type[randint(0, len(n_type)-1)][:-3] + di.get(part), di, part
    else:
        return corr[part], n_type[randint(0, len(n_type)-1)][:-2] + di.get(part), di, part
# e.g.(nominative plural, ναυται, d1_vautns, 1)


def rand_exc_case(exclude):
    lst = list(corr.keys())
    lst.remove(exclude[3])
    ans = []
    count = 3
    while count > 0:
        temp = choice(lst)
        if exclude[2][temp] == exclude[2][exclude[3]]:
            lst.remove(temp)
            continue
        ans.append(corr[temp])
        lst.remove(temp)
        count -= 1
    return tuple(ans)
