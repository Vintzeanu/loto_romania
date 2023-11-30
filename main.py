import random

varianta = input('Cate numere vrei să afișez: \n')
limita = input('Din câte vrei să fie: \n')

def loto(varianta, limita):
    numere = set()
    while len(numere) < int(varianta):
        numere.add(random.randint(1, int(limita)))
    loto = list(numere)
    return loto

print(loto(varianta, limita))
