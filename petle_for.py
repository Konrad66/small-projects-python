# petla for inaczej petla obiektowa

moja_lista = [1, 2, 3, 4, 5]
i = 0
while i < len(moja_lista):
    print(moja_lista[i])
    i += 1

# x to zmienna iteracyjna (iterator),
# która w każdym obiegu pętli przyjmuje wartość kolejnego elementu z listy moja_lista.
# przez zmienna x w kolekcji iteruj
for x in moja_lista:
    print(x)

# pętla for z range
print(range(10))

# mozemy przekonwertowac range na liste
# mozemy powiedziec ze funkcja range buduje nam tak jakby liste
# (poniewaz ja sobie przekonwertowalismy na typ listy) z uzupelnionymi wartosciami
print(list(range(10)))

# w tym przypadku pętla wykona się zawsze tyle razy ile wynosi liczba range
for y in range(10):
    print(y)

# w funkcji range mozemy okreslic dodatkowo dwa argumenty
# range (poczatkowa wartosc, ilosc elementow range)
for y in range(1, 11):
    print(y)

# trzecim argumentem funkcji range
# range (poczatkowa wartosc, ilosc elementow range, o ile elementow chcemy przeskakiwac w funkcji)
for y in range(1, 11, 2):
    print(y)
