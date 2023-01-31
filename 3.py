dictionary_pravoagolnik = dict()
strana_1 = int(input("Vnesi dolzina: "))
strana_2 = int(input("Vnesi shirina: "))

dictionary_pravoagolnik["Shirina"] = strana_1
dictionary_pravoagolnik["Dolzina"] = strana_2

plostina = strana_1 * strana_2
dictionary_pravoagolnik["Plostina"] = plostina

perimetar = 2 * (strana_1 + strana_2)
dictionary_pravoagolnik["Perimetar"] = perimetar

if (plostina > perimetar):
    dictionary_pravoagolnik["Pogolem"] = "Plostina"
else:
    dictionary_pravoagolnik["Pogolem"] = "Perimetar"

print("Printanje na dictionary pravoagolnik ",dictionary_pravoagolnik)