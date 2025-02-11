#ostatnia kolejca w python jest tak zwana krotka (tupla)
#krotka w odróznieniu do list czy słowników jest stałą kolekcją tzn że nie możemy modyfikować elementów
#które się w niej znajdują

#krotkę definiujemy za pomocą nawiasów okrągłych
krotka = (3, 9, 27, 81, 243, 729)

#aby odwołać się do konkretnego elementu w krotce, używamy tak jak do tej pory używaliśmy
# w listach i słownikach używamy nawiasu []
# no i pierwszy element jest zawsze o indeksie 0
print(krotka[0])
print(krotka[4])

print(krotka)

#krotka moze przechowywać różne typy danych nie tylko liczbowe, krotkę możemy przyrównać do list,
mieszana_tupla = (1, "tekst", 3.14, True)
jednoelementowa_tupla = (42,)  # przecinek jest wymagany
#można również w niej przechowywać zduplikowane elementy



# które już poznaliśmy jakiś czas temu, jest jednak kilka róznic


# i taką największą różnica jaka jest miedzy krotka a listami
# jest taka że nie możemy w taki sam sposób zmienić elementu kolekcji
#krotka[0] = 1 -> wyskoczy błąd, błąd w skrócie mówi o tym że krotka nie wspiera modyfikacji swoich elementów
# co oznacza że raz zadeklarowane wartości w krotce nie są już do modyfikacji
#nie można do niej dodawać również nowych elementów ani usuwać

#krotka oferuje nam również mniej funkcji które możemy na niej wywoływać




#len() – Zwraca liczbę elementów w tupli:
moja_tupla = (1, 2, 3)
print(len(moja_tupla))

#count() – Zlicza wystąpienia danego elementu:
print(krotka.count(3))


#index() – Zwraca indeks pierwszego wystąpienia danego elementu:
print('index ', krotka.index(9))

#tuple() – Tworzy tuplę z innego obiektu iterowalnego:
lista = [1, 2, 3]
nowa_tupla = tuple(lista)  # (1, 2, 3)


#Nie można ich przypadkowo zmodyfikować – dzięki temu są bardziej odporne na błędy.
#Szybsze niż listy – operacje na tuplach są bardziej wydajne, ponieważ są przechowywane w bardziej zwartej formie.
#Bezpieczne jako klucze w słownikach – Dzięki niezmienności można używać ich jako kluczy w słownikach
# lub elementów zbiorów.

print(krotka)



#Przechowywanie rekordów o stałej strukturze:
osoba = ("Jan", "Kowalski", 30)  # imię, nazwisko, wiek


#Zwracanie wielu wartości z funkcji:
def koordynaty():
    return (10, 20)

x, y = koordynaty()
print(x, y)  # 10, 20



#Klucze w słownikach:
dane = {("Jan", "Kowalski"): "adres1", ("Anna", "Nowak"): "adres2"}
print(dane[("Jan", "Kowalski")])  # "adres1"


#Stałe dane: Jeśli dane nie powinny być zmieniane w trakcie działania programu, można użyć tupli zamiast list.