#tworzenie list
#lista = []

#lista może przechowywać różne typy danych
#lista = [1, 2, "c", "d"]

#w liście po przecinku nie musimy podawać danych, nie wyskoczy błąd
#lista = [1, 2, "c", "d", ]


#pierwsza wartość listy zaczyna się od zera
lista = [1, 2, "c", "d", ]
print(lista[3])
print(lista)


#w celu zmiany elementu listy, musimy się odwołać do elementu który chcemy zmienić
# i przypisać poprzez = nową wartość, która może być innego typu
lista[2] = 3
print(lista)

#ciekawostka, typ string jest przechowywany w podobny sposób co lista
# i można się do niej odwołać również za pomocą odwołania do kontretnego indexu
#Stringa jedynie nie można modyfikowac w ten sposób
text = "hej"
print(text[1])

#listy mozemy łączyć z innymi listami, w tym przypadku lista nie zmieni swojego rozmiaru
print(lista + ["e", 6])

#listy mozemy mnożyć co powieli nam liste x razy
print(lista * 2)

#możemy wyświetlić liczbe elementów w liście (tak zwaną długość)
print("ilość elementów: ", len(lista))

#dodaje nam do listy nowy element, dodaje go na koniec listy
lista.append("g")
#za pomoca append mozemy dodac nowa liste do listy
lista.append([8,9])
print(lista)

#oznacza to ze mamy liste w liście i aby się odwołac do listy w liscie,
#musimy wskazać element tej drugiej listy i później znowu wskazać kolejny element
print(lista[5][1])

#insert dołącza element we  wskazanym przez nas indexie
#najpierw wskazujemy index w którym miejscu chcemy wstawić nowy element
lista.insert(3, 3)
print(lista)
print(len(lista))

#metoda count moze nam policzyć ilość wystapień danego elementu z listy
print("ilość: ", lista.count(3))

#w tym przypadku metoda zwróci index pod którym znajduje sie dany element
print("Index: ", lista.index("g"))

#metoda remove pozwala nam na usunięcie konkretnego elementu z listy
lista.remove("g")
print(lista)

#w przypadku list w ktorych mamy wartości liczbowe, mozemy zwracać najmniejszy i największy element
lista2 = [1, 2, 3, 66, 4, 5, -1,]
print("Min: ", min(lista2))
print("Min: ", max(lista2))

#możemy podosrtować listę od najmniejsz do najwiekszej wartości za pomocą metody sort
lista2.sort()
print(lista2)

#kolejna metoda to odwrócenie listy
lista2.reverse()
print(lista2)

#metoda ktora pozwala nam czyscic elemnty listy
lista2.clear()
print(lista2)









#zadanie napisz pętle while która wyświetli elementy listy, tak długo jak długa jest lista
# moja_lista = [1, 2, 3, 4, 5]
# i = 0
# while i < len(moja_lista):
#     print(moja_lista[i])
#     i+= 1
