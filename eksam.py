#Selle töö jaoks impordin os.path, mis aitab mul faile manipuleerida - Erik Pavlovitšev IT19E
import os.path

million = 100000

def calculate():

    fail_a = os.path.exists("a.txt")
    fail_b = os.path.exists("b.txt")

    if fail_a == True:
        with open("a.txt") as f:
            esimene_number = f.readline()
    if fail_b == True:
        with open("b.txt") as f:
            teine_number = f.readline()

    summa = int(esimene_number) + int(teine_number)
    summa1 = str(summa)

    if summa > million:
        with open("miljon22r.txt") as f:
            f.write(summa1)
    else:
        with open("summa.txt") as f:
            f.write(summa1)

    i = summa
    while i < 20:
        print("Tere!")
        i += 1


calculate()