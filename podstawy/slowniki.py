# słownik składa się z par wartości,
# jedną wartością jest klucz (np słowo po jakim szukamy w naszym słowniku)
# drugą wartością w słowniku jest objaśnienie klucza inaczej wartość

# Kluczem może być dowolny typ danych
# wartość dla klucza nadajemy po użyciu :

# każda z tych wartości jest parą wartości

slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela" }


#aby wybrać wartość ze słownika, używamy już nawiasów kwadratowych a nie klamr, w nawiasie odnosimy się już do klucza z pod jakiego chcemy wyciągnąc naszą wartość

print(slownik)
print(slownik[1])
print(slownik[7])


# aby dodać wartość do słownika wystarczy pod odpowiedni numer klucza przypisa wartość
# dictionary (słownik) nie jest sortowany, wartości dodawane są na koniec słownika
# Słownik nie musi posiadać jednego typu wartości, możemy dodawać do niego tak samo jak w liście różne typy
slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 5

#Kluczem mogą również być osobne typy danych
slownik["a"] = 1


#w przypadku kiedy chcemy się odnieść do klucza w słowniku którego nie mamy, consola wyrzuci nam błąd
print(slownik[8])

#i tutaj słownika możemy użyć w ciekawy sposób, i odnieść się do elementu ktory nie istnieje
# i jeżeli nie znajdzie w słowniku klucza o podanek wartości wyświetli komunikat,
# który mu zadeklarujemy, możemy podać opcjonalny parametr, który zostanie wyświetlony jak nie znajdzie wartości
print(slownik.get(8, "inny dzień"))


#teraz wyświetlmy sobie nasz słownik element po elemencie w nowej lini:
print("\n Pętla: ")
for i in slownik.v:
	print(i)

#Domyślnie pętla for iteruje po wartościach kluczy w słowniku, aby to zmienić możemy odwołać się bezpośrednio do wartości jakie chcemy wyświetlić

slownik.keys()
slownik.values()

#usuwanie z słownika, do usuwania słownika, używamy funkcji, która nazwya się pop
slownik.pop(1)
