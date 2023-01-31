dictionary_broevi = dict()
broj1 = int(input("Vnesi go prviot broj: "))
broj2 = int(input("Vnesi go vtoriot broj: "))

dictionary_broevi["Prv_broj"] = broj1
dictionary_broevi["Vtor_broj"] = broj2

zbir = broj1+broj2
dictionary_broevi["Zbir"] = zbir

odzemanje = broj1-broj2
dictionary_broevi["Odzemanje"] = odzemanje

mnozenje = broj1 * broj2
dictionary_broevi["Mnozenje"] = mnozenje

delenje = broj1 / broj2
dictionary_broevi["Delenje"] = delenje

print("Printanje na dictionary ",dictionary_broevi)

