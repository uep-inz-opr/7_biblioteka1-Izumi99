class Biblioteka:
    def __init__(self, tytul, autor, ilosc_ksiazek = 1):
        self.tytul = tytul
        self.autor = autor
        self.ilosc_ksiazek = ilosc_ksiazek

    ksiazki = []

    def __repr__(self):
        return f"('{self.tytul}, '{self.autor}', {self.ilosc_ksiazek})"

    def sprawdz_egzemplarz(tytul, autor):
        if Biblioteka.ksiazki != []:
            j = 0
            while j < len(Biblioteka.ksiazki):
                if Biblioteka.ksiazki[j][0] == tytul:
                    Biblioteka.ksiazki[j][2] = Biblioteka.ksiazki[j][2] + 1
                    break

                if Biblioteka.ksiazki[j][2] != tytul and j+1 == len(Biblioteka.ksiazki):
                    Biblioteka.ksiazki.append([tytul, autor, 1])
                    break

                j = j + 1

        else:
            Biblioteka.ksiazki.append([tytul, autor, 1])


class Egzemplarz():
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self. autor = autor
        self.rok = rok
        Biblioteka.sprawdz_egzemplarz(self.tytul, self.autor)

    def __repr__(self):
        return f"('{self.tytul}, '{self.autor}', {self.rok})"

i = input()
for ksiazka in range(int(i)):
    x = eval(input())
    Egzemplarz(x[0], x[1], x[2])

Biblioteka.ksiazki = sorted(Biblioteka.ksiazki, key=lambda x: x[0])

j = 0
while j < len(Biblioteka.ksiazki):
    print(Biblioteka(Biblioteka.ksiazki[j][0], Biblioteka.ksiazki[j][1], Biblioteka.ksiazki[j][2]))
    j = j + 1