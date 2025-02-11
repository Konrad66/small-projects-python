def multiply(x):
    return x * x


# Funkcja może być przekazywana w zwykłej zmiennej

wynik = multiply
print(wynik(5))


def func(f1, x):
    return f1(x) * x


print(func(multiply, 5))


# i teraz przejdziemy sobie do rekurencji funkcji
# i popularnym przykładem jest tutaj silnia
# Silnia liczby n oznacza mnożenie wszystkich liczb całkowitych od 1 do n.
# Można więc powiedzieć, że silnia to iloczyn kolejnych liczb naturalnych
# silnie oznacza się znakiem !
# moglibyśmy to robić pętlą while -> jest to prawidłowe
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

print(silnia(5))