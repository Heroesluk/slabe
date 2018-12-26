sem = []
for i in range(81):  ##Tworzy tablice 81 znakow
   sem.append("O")


def drukowanko():
    for index, item in enumerate(sem, start=1):
        print item,  ##Drukuje ja w formacie 9x9
        if not index % 9:
            print

drukowanko()

class statek:
    def __init__(self, x,y,hp):
        self.x = x
        self.y = y        ##tworzy klase statek, x i y to kordynaty, hp to ilosc pol statku, zywa
        self.hp = hp

    def info(self):
        print(self.x, self.y, "hp wynosi",self.hp) ##wyswietla informacje

class pancernik:
    def __init__(self, x, y, x1, y1, hp):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.hp = hp

    def info(self):
        print(self.x, self.y,  self.x1, self.y1, "hp wynosi",self.hp) ##wyswietla informacje


def sprawdz():
    print("Podaj koordynaty x a potem y strzalu")
    x = input()
    y = input()
    if yamato.x == x and yamato.y == y:

        print("Trafiles")
        yamato.hp = yamato.hp - 1
        if yamato.hp == 0:
            print"Zatopiles"
            sem[yamato.y * 9 - (10 - yamato.x)] = "Z"
        yamato.info()
    elif yamikaze.x == x and yamikaze.y == y:

        print("Trafiles")
        yamikaze.hp = yamikaze.hp - 1
        if yamikaze.hp == 0:
            print("zatopiles")
            sem[yamikaze.y * 9 - (10 - yamikaze.x)] = "Z"
        yamikaze.info()

    elif stefani.x == x and stefani.y == y:

        print("Trafiles")
        stefani.hp = stefani.hp - 1
        if stefani.hp == 0:
            print("zatopiles")
            sem[stefani.y * 9 - (10 - stefani.x)] = "Z"
            sem[stefani.y1 * 9 - (10 - stefani.x1)] = "Z"
        else:
            sem[stefani.y * 9 - (10 - stefani.x)] = "T"
        stefani.info()

    elif stefani.x1 == x and stefani.y1 == y:

        print("Trafiles")
        stefani.hp = stefani.hp - 1
        if stefani.hp == 0:
            print("zatopiles")
            sem[stefani.y1 * 9 - (10 - stefani.x1)] = "Z"
            sem[stefani.y * 9 - (10 - stefani.x)] = "Z"

        else:
            sem[stefani.y1 * 9 - (10 - stefani.x1)] = "T"


        stefani.info()


    else:
        print("Nie trafiles")
        sem[y * 9 - (10 - x)] = "X"



print("Podaj koordynaty x a potem y swojego statku")
yamato = statek(input(),input(),1)
yamato.info()

print("Podaj koordynaty x a potem y swojego statku")
yamikaze = statek(input(),input(),1)
yamikaze.info()

print("Podaj koordynaty pierwszego pola, a potem drugiego pola pancernika")
stefani = pancernik(input(),input(),input(),input(),2)
stefani.info()


sprawdz()
drukowanko()
sprawdz()
drukowanko()
sprawdz()
drukowanko()