# funkcje w języku python

# przykładowo funkcja którą do tej pory wykorzystywaliśmy to print(),
# która po przeyjęciu argumentu (dowolny typ danej) wydrukuje nam na ekranie ten typ

#w taki sposób wywołuje się funkcje
print("hej")
#jednym z założeń funckji jest - Don't repeat your self - czyli nie powtarzaj się

#funkcja pozwala nam zagregować pewien algorytm/ pewne zadanie do wykonania
#w postaci nazwy i umożliwić nam wywołanie jej niskończenie wiele razy
#czyli w skórcie pozwala nam zaoszczędzić wiele linijek kodu

#aby wyznaczyć funkcje w python trzeba użyć słówka w postaci 'def' co jest rozwinieńciem  definicji (definition)


#nawias jest zarezerwowany dla argumentów
def funkcaj_test():
    print("W tej funckji drukujemy napis")

#aby wywołać funkcje odnosimy się do jej nazwy
#ważna rzecz, nie można wywołać funkcji przed jest deklaracją
funkcaj_test()




#kolejnym przykładem funkcji jest funkcja z argumentami

def dodawanie(x):
    print(x + 1)
#poza funkcją wartość stworzona w tym przypadku x nie istnieje


dodawanie(2)

#czy możemy deklarować więcej argumentów? oczywiście że tak
def dodawanie(x, y):
    print(x + y)

dodawanie(2, 5)
#dodawanie(2)
# w tym przypadku będzie błąd, żeby uniknąć takiego błędu, możemy jeden z warunków zadeklarować jako opcjonalny
def dodawanie(x, y = 1):
    print(x + y)
#po zadeklarowaniu argumentu opcjonalnego, nie mozemy już zadeklarować kolejnego argumentu,
# który trzeba zadeklarować, musi to być również argument opcjonalny
dodawanie(2)

def dodawanie(x, y = 1, z = 0):
    print(x + y + z)

dodawanie(3)





#return służy za zwracanie tej wartości z funkcji poza ramy tej funkcji,
# czyli jak wczesniej nie mogliśmy się odnieść do x lub innych argumentów to teraz też nie możemy
#ale za to wynik tego działania możemy zapisac do innej zmiennej
def dodawanie(x, y = 1, z = 0):
    return x + y + z

print(dodawanie(2))
wynik = dodawanie(2,4,5)
print(wynik)


#no i tutaj możemy zobaczyć przykład błędny bez returna
def dodawanie(x):
    print(x+1)
wynik2 = dodawanie(2)
#return jest tak zwaną instrukcją skoku

#i tutaj taka ciekawosta z returnem
def dodawanie(x):
    return x + 1
    print(x+1) #to nigdy nie dojdzie do skutku, do działania

lista6 = [1, [2, 3], [4, [5, 6]]]
lista_plaska = []

for element in lista6:
    if isinstance(element, list):
        lista_plaska.extend(lista6)
    else:
        lista_plaska.append(element)

lista_dzialan = []
lista_dzialan.append(dodawanie(), )