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
yes = '[ἀ, Ἑ, ἐ, ἱ, ἰ, ὀ, ὑ, ἡ, ἠ, ῥ]'
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
n3_gerwv = ("γερων",)
n3_avnr = ("ἀνηρ",)
n3_patnr = ("πατηρ", "μητηρ")
n3_thugatnr = ("θυγατηρ",)
n3_elpis = ("ἐλπις",)
n3_pous = ("πους",)
n3_rntwr = ("ῥητωρ",)
n3_guvn = ("γυνη",)
n3_polis = ("πολις",)
n3_presbus = ("πρεσβυς",)
n3_astu = ("ἀστυ",)
n3_basileus = ("βασιλευς",)
n3_bous = ("βους",)
n3_ofrus = ("ὀφρυς",)
n3_vaus = ("ναυς",)
n3_graus = ("γραυς",)
n3_pelekus = ("πελεκυς",)
n3_teixos = ("τειχος",)
n3_plnthos = ("πληθος",)
n3_odous = ("ὀδους",)
n3_gigas = ("γιγας",)
n3_ngemwv = ("ἠγεμων",)
n3_thnr = ("θηρ",)
n3_nrws = ("ἡρως",)
n3_xeir = ("χειρ",)
n3_orvis = ("ὀρνις",)
n3_udwr = ("ὑδωρ",)
n3_erws = ("ἐρως",)
n3_xaris = ("χαρις",)
n3_vuks = ("νυξ",)
n3_sus = ("συς",)
n3_dakru = ("δακρυ",)
n3_leimwv = ("λειμων",)
n3_uios_a = ("υἱος",)
n3_uios_b = ("υἱος",)
n3_ellnv = ("Ἑλλην",)
n3_ellas = ("Ἑλλας",)
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
d3_avnr = {1: "ηρ", 2: "δρα", 3: "δρος", 4: "δρι", 5: "δρες", 6: "δρας", 7: "δρων", 8: "δροσι(ν)"}
d3_patnr = {1: "ηρ", 2: "ερα", 3: "ρος", 4: "ρι", 5: "ερες", 6: "ερας", 7: "ερων", 8: "ρασι(ν)"}
d3_thugatnr = {1: "ηρ", 2: "ερα", 3: "ρος", 4: "ρι", 5: "ερες", 6: "ερας", 7: "ερων", 8: "ρασι(ν)"}
d3_elpis = {1: "ις", 2: "ιδα", 3: "ιδος", 4: "ιδι", 5: "ιδες", 6: "ιδας", 7: "ιδων", 8: "ιδσι(ν)"}
d3_pous = {1: "υς", 2: "δα", 3: "δος", 4: "δι", 5: "δες", 6: "δας", 7: "δων", 8: "σι(ν)"}
d3_rntwr = {1: "ωρ", 2: "ορα", 3: "ορος", 4: "ορι", 5: "ορες", 6: "ορας", 7: "ορων", 8: "ορσι(ν)"}
d3_guvn = {1: "νη", 2: "ναικα", 3: "ναικος", 4: "ναικι", 5: "ναικες", 6: "ναικας", 7: "ναικων", 8: "ναιξι(ν)"}
d3_polis = {1: "ις", 2: "ιν", 3: "εως", 4: "ει", 5: "εις", 6: "εις", 7: "εων", 8: "εσι(ν)"}
d3_presbus = {1: "υς", 2: "υν", 3: "εως", 4: "ει", 5: "εις", 6: "εις", 7: "εων", 8: "εσι(ν)"}
d3_astu = {1: "τυ", 2: "τυ", 3: "τεως", 4: "τει", 5: "τη", 6: "τη", 7: "τεων", 8: "τεσι(ν)"}
d3_basileus = {1: "υς", 2: "α", 3: "ως", 4: "ι", 5: "ις", 6: "ας", 7: "ων", 8: "υσι(ν)"}
d3_bous = {1: "υς", 2: "υν", 3: "ος", 4: "οι", 5: "ες", 6: "υς", 7: "ων", 8: "ουσι(ν)"}
d3_ofrus = {1: "υς", 2: "υν", 3: "υος", 4: "υι", 5: "υες", 6: "υς", 7: "υων", 8: "υσι(ν)"}
d3_vaus = {1: "αυς", 2: "αυν", 3: "εως", 4: "ηι", 5: "ηες", 6: "αυς", 7: "εων", 8: "αυσι(ν)"}
d3_graus = {1: "υς", 2: "υν", 3: "ος", 4: "ι", 5: "ες", 6: "υς", 7: "ων", 8: "υσι(ν)"}
d3_pelekus = {1: "υς", 2: "υν", 3: "εως", 4: "ει", 5: "εις", 6: "εις", 7: "εων", 8: "εσι"}
d3_teixos = {1: "ος", 2: "ον", 3: "ους", 4: "ει", 5: "η", 6: "η", 7: "ων", 8: "εσι(ν)"}
d3_plnthos = {1: "ος", 2: "ος", 3: "ους", 4: "ει", 5: "η", 6: "η", 7: "ων", 8: "εσι(ν)"}
d3_odous = {1: "υς", 2: "ντα", 3: "ντος", 4: "ντι", 5: "ντες", 6: "ντας", 7: "ντων", 8: "ουσι(ν)"}
d3_gigas = {1: "ας", 2: "αντα", 3: "αντος", 4: "αντι", 5: "αντες", 6: "αντας", 7: "αντων", 8: "ασι(ν)"}
d3_ngemwv = {1: "ων", 2: "ονα", 3: "ονος", 4: "ονι", 5: "ονες", 6: "ονας", 7: "ονων", 8: "οσι(ν)"}
d3_thnr = {1: "ηρ", 2: "ηρα", 3: "ηρος", 4: "ηρι", 5: "ηρες", 6: "ηρας", 7: "ηρων", 8: "ηρσι(ν)"}
d3_nrws = {1: "ως", 2: "ωα", 3: "ωος", 4: "ωι", 5: "ωες", 6: "ωας", 7: "ωων", 8: "ωσι(ν)"}
d3_xeir = {1: "ιρ", 2: "ιρα", 3: "ιρος", 4: "ιρι", 5: "ιρες", 6: "ιρας", 7: "ιρων", 8: "ρσι(ν)"}
d3_orvis = {1: "ις", 2: "ιν", 3: "ιθος", 4: "ιθι", 5: "ιθες", 6: "ιθας", 7: "ιθων", 8: "ισι(ν)"}
d3_udwr = {1: "ωρ", 2: "ωρ", 3: "ατος", 4: "ατι", 5: "ατα", 6: "ατα", 7: "ατων", 8: "ασι(ν)"}
d3_erws = {1: "ως", 2: "ωτα", 3: "ωτος", 4: "ωτι", 5: "ωτες", 6: "ωτας", 7: "ωτων", 8: "ωσι(ν)"}
d3_xaris = {1: "ις", 2: "ιν", 3: "ιτος", 4: "ιτι", 5: "ιτες", 6: "ιτας", 7: "ιτων", 8: "ισι(ν)"}
d3_vuks = {1: "ξ", 2: "κτα", 3: "κτος", 4: "κτι", 5: "κτες", 6: "κτας", 7: "κτων", 8: "ξι(ν)"}
d3_sus = {1: "υς", 2: "υν", 3: "υος", 4: "υι", 5: "υες", 6: "υς", 7: "υων", 8: "υσι(ν)"}
d3_dakru = {1: "υ", 2: "υ", 3: "υος", 4: "υι", 5: "υα", 6: "υα", 7: "υων", 8: "υσι(ν)"}
d3_leimwv = {1: "ων", 2: "ωνα", 3: "ωνος", 4: "ωνι", 5: "ωνες", 6: "ωνας", 7: "ωνων", 8: "ωσι(ν)"}
d3_uios_a = {1: "ος", 2: "ον", 3: "ου", 4: "ῳ", 5: "οι", 6: "ους", 7: "ων", 8: "οις"}
d3_uios_b = {1: "ος", 2: "ον", 3: "εος", 4: "ει", 5: "εις", 6: "εις", 7: "εων", 8: "εσι(ν)"}
d3_ellnv = {1: "ην", 2: "ηνα", 3: "ηνος", 4: "ηνι", 5: "ηνες", 6: "ηνας", 7: "ηνων", 8: "ησι(ν)"}
d3_ellas = {1: "ας", 2: "αδα", 3: "αδος", 4: "αδι", 5: "αδες", 6: "αδας", 7: "αδων", 8: "ασι(ν)"}
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
    n3_gerwv: d3_gerwv,
    n3_avnr: d3_avnr,
    n3_patnr: d3_patnr,
    n3_thugatnr: d3_thugatnr,
    n3_elpis: d3_elpis,
    n3_pous: d3_pous,
    n3_rntwr: d3_rntwr,
    n3_guvn: d3_guvn,
    n3_polis: d3_polis,
    n3_presbus: d3_presbus,
    n3_astu: d3_astu,
    n3_basileus: d3_basileus,
    n3_bous: d3_bous,
    n3_ofrus: n3_ofrus,
    n3_vaus: d3_vaus,
    n3_graus: d3_graus,
    n3_pelekus: d3_pelekus,
    n3_teixos: d3_teixos,
    n3_plnthos: d3_plnthos,
    n3_odous: d3_odous,
    n3_gigas: d3_gigas,
    n3_ngemwv: d3_ngemwv,
    n3_thnr: d3_thnr,
    n3_nrws: d3_nrws,
    n3_xeir: d3_xeir,
    n3_orvis: d3_orvis,
    n3_udwr: d3_udwr,
    n3_erws: d3_erws,
    n3_xaris: d3_xaris,
    n3_vuks: d3_vuks,
    n3_sus: d3_sus,
    n3_dakru: d3_dakru,
    n3_leimwv: d3_leimwv,
    n3_uios_a: d3_uios_a,
    n3_uios_b: d3_uios_b,
    n3_ellnv: d3_ellnv,
    n3_ellas: d3_ellas
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
    n3_gerwv: d3_gerwv,
    n3_avnr: d3_avnr,
    n3_patnr: d3_patnr,
    n3_thugatnr: d3_thugatnr,
    n3_elpis: d3_elpis,
    n3_pous: d3_pous,
    n3_rntwr: d3_rntwr,
    n3_guvn: d3_guvn,
    n3_polis: d3_polis,
    n3_presbus: d3_presbus,
    n3_astu: d3_astu,
    n3_basileus: d3_basileus,
    n3_bous: d3_bous,
    n3_ofrus: d3_ofrus,
    n3_vaus: d3_vaus,
    n3_graus: d3_graus,
    n3_pelekus: d3_pelekus,
    n3_teixos: d3_teixos,
    n3_plnthos: d3_plnthos,
    n3_odous: d3_odous,
    n3_gigas: d3_gigas,
    n3_ngemwv: d3_ngemwv,
    n3_thnr: d3_thnr,
    n3_nrws: d3_nrws,
    n3_xeir: d3_xeir,
    n3_orvis: d3_orvis,
    n3_udwr: d3_udwr,
    n3_erws: d3_erws,
    n3_xaris: d3_xaris,
    n3_vuks: d3_vuks,
    n3_sus: d3_sus,
    n3_dakru: d3_dakru,
    n3_leimwv: d3_leimwv,
    n3_uios_a: d3_uios_a,
    n3_uios_b: d3_uios_b,
    n3_ellnv: d3_ellnv,
    n3_ellas: d3_ellas
}
# aidws, Zeus, other names


def rand_all():
    n_type = choice(list(dct_all.keys()))
    part = randint(1, 8)
    di = dct_all.get(n_type)
    base = n_type[randint(0, len(n_type)-1)]
    if n_type in [n3_swma, n1_fwvn, n1_tolma, n1_xwra, n3_dakru, n3_vuks]:
        return corr[part], base[:-1] + di.get(part), di, part, base
    elif n_type in [n2_vous, n2_ostouv, n3_vaus]:
        return corr[part], base[:-3] + di.get(part), di, part, base
    else:
        return corr[part], base[:-2] + di.get(part), di, part, base
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

