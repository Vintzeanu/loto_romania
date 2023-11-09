import random

numar = input('pentru 5/40 apasă 5, pentru 6 din 49 apasă 6\n')


def loto_sase_dinpatruzecisinoua():
    sase_numere = set()
    while len(sase_numere) < 6:
        sase_numere.add(random.randint(1, 49))
    loto = list(sase_numere)
    return loto


# print(loto_sase_dinpatruzecisinoua())

def loto_cinci_dinpatruzeci():
    cinci_numere = set()
    while len(cinci_numere) < 5:
        cinci_numere.add(random.randint(1, 40))
    loto = list(cinci_numere)
    return loto


# print(loto_cinci_dinpatruzeci())


if numar == '5':
    print(loto_cinci_dinpatruzeci())
elif numar == '6':
    print(loto_sase_dinpatruzecisinoua())
else:
    print('trebuie să introduci 5 pentru 5/40 sau 6 pentru 6/49')