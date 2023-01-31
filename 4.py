prodavnica = dict()

prodavnica['Produkti'] = list()
prodavnica['Ceni'] = list()
plati = 0
while True:
    produkt = input("Vnesi produkt: ")
    prodavnica['Produkti'].append(produkt)
    cena = int(input("Vnesi cena: "))
    prodavnica["Ceni"].append(cena)
    da_ne = input("Dali ke prodolzite (da/ne) ")
    if (da_ne == "ne"):
        break;

vkupno = sum(prodavnica['Ceni'])
prodavnica["Vkupno"] = vkupno
plakjanje = input("Dali ke plakjate? (da/ne)")
if (plakjanje == "da"):
    while True:
        if (plati < vkupno):
            print("Vasata smetka iznesuva ",prodavnica["Vkupno"])
            plati = int(input("Vnesi uplakanje: "))
        else:
            break
    kusur = plati - vkupno
    if (kusur > 0):
        prodavnica["kusur"] = kusur
    else:
        prodavnica["plateno"] = "plateno"

print("Celata prodavnica e ", prodavnica)
