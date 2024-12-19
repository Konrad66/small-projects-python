# zmienne logiczne (dla przypomnienia zmienne w Python nie posiadają typów, ale zmienne domyślają się jakiego są typu)
c = True
y = False
# zmienne True i False piszemy zawsze z dużej litery
print(c)
print(y)

# operatory porównia - sprawdza czy lewa storna jest równa prawej
# i w zależnosci od tego wyniku zwraca nam odpowiedni typ logiczny (w tym przypadku True lub False)
print(5 == 5)

# operator różne - czy lewa strona jest różna od prawej
print(5 != 1)
# operator większy
print(7 > 5)
# operator mniejszy
print(7 < 5)

# operator mniejszy równy
print(7 <= 5)
# operator większy bądź równy
print(7 >= 5)

# operatory porównania wykorzystujemy w intrukcjach warunkowych IF
# instrukcje warunkowe

# if możemy sobie przetłumaczyć jako jeżeli
# instrukcja warunkowo if
if 5 == 5:
    print("Prawda")

# else mozemy przetłumaczyć jako w przeciwnym wypadku w przeciwnym razie
if 15 > 5:
    print("Wieksze")
else:
    print("mniejsze")

a = 5
b = 10

if a > b:
    print("Wieksze")
elif a < b:
    print("mniejsze")
else:
    print("Równe")

age = 19
money = 55

if age >= 13:
    print("Możesz wejść do kina.")
    if money >= 35:
        print("Tutaj bilet na seans. Miłego seansu!")
    else:
        print("Musisz kupić bilet, aby wejść.")
else:
    print("Jesteś za młody, aby wejść do kina bez opiekuna.")

# zagnieżdzanie instrukcji warunkowych
age = 19
money = 40

if age >= 13:
    print("Możesz wejść do kina.")
    if money >= 35:
        print("Tutaj bilet na seans. Miłego seansu!")
    else:
        print("Musisz kupić bilet, aby wejść.")
else:
    print("Jesteś za młody, aby wejść do kina bez opiekuna.")

# operatory logiczne

#and - i czyli oba są spełnione
if age >= 18 and money >= 35:
    print("Możesz wejść do kina")

#or (lub) - zwraca True jeśli jeden z warunków jest spełniony
if age <= 12 or money >= 30:
    print("Możesz wejść do kina")
#w przypadku or zawsze sprawdza pierwszy warunek, jeżeli jest nie spełniony to dopiero przechodzi do drugiego w innym wypadku jest pomijany


#ostatnio operator logiczny działa tylko na jedno argumentowy - działa tylko na pojedynczej wartości logicznej True lub False
#co możemy zrobić na pojedynczej wartości logicznej, zanegować ją
#operator negacji
if not age > 12 or money >= 30:
    print("możesz wejść")

#operatory logiczne mają swoją wagę

if True or False and False:
    print("Prawda")

#operatory logiczne mają swoją wagę (priorytet) i mają również swoje konretną kolejność wykonywania
#not (najwyższy priorytet)
#and (średni priorytet)
#or (najniższy priorytet)

if (True or False) and False:
    print("Prawda")
else:
    print("Fałsz")