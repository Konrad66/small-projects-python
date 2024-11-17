### Zadanie dla chętnych.
##      Wygeneruj listę 1000-elementową zaczynającą się od 1 i kończącą na 1000,
##      a następnie na trzy różne sposoby indeksowania znajdź element równy 999.

lista1 = list(range(1, 1001))

element_1 = lista1[998]
element_2 = None
for i in lista1:
    if i == 999:
        element_2 = i
        break
index_999 = lista1.index(999)
element_3 = lista1[index_999]



### Zadanie 1.
##      Za pomocą pętli for zmień rozszerzenia plików z listy files
##      aby otrzymać rozszerzenia ".csv" w miejsce ".txt". Zapisz nowe
##      nazwy plików w liście files_changed.
##      Skorzystaj ze sposobu tradycyjnego (z wcięciami) oraz
##      list comprehension.

files = ["dtype.txt",
         "file_user.txt",
         "https://www.raportmniejszosci.txt",
         "dataset.txt"]

files_changed = []
for file in files:
    if file.endswith(".txt"):
        files_changed.append(file.replace(".txt", ".csv"))

# 2. List comprehension
files_changed_lc = [file.replace(".txt", ".csv") for file in files if file.endswith(".txt")]


### Zadanie 2.
##      Z podanej listy za pomocą pętli for i warunku if wydobądź
##      elementy, które spełniają poniższe kryteria.
##      Wynik zapisz jako nową listę.

list_1 = ['La', 'Chanson', 3.0, 'de', 12, 'Mardi', 87, 'Gras', 36,
            'Ich', 'mochte' , 51, 'wie', 'Herr', 138.0,
            'Weber', 'werden!', 4, 20.0]

#A są typu string.

result_A = [el for el in list_1 if isinstance(el, str)]
print(result_A)

#B są typu string i składają się z co najmniej 4 liter.
result_B = [el for el in list_1 if isinstance(el, str) and len(el) >= 4]
print(result_B)

#C są dowolnymi liczbami.
result_C = [el for el in list_1 if isinstance(el, (int, float))]
print(result_C)

#D są liczbami podzielnymi przez 4, ale nie przez 8.
result_D = [el for el in list_1 if isinstance(el, int) and el % 4 == 0 and el % 8 != 0]
print(result_D)



### Zadanie 1.
#   Skorzystaj z pętli for i warunku ifelse aby,
#   poczynając od pierwszego elementu,
#   z podanej listy dokonać odejmowanie kolejnych elementów od
#   dotychczasowego wyniku. Rezultat cząstkowych wyliczeń zachowaj do nowej
#   listy. Tj. pierwszy element nowej listy to będzie 3123, bo 3123 - 0 = 3123;
#               drugi element to 2044, bo 3123 - 1079 == 2044;
#               trzeci element to 1039, bo 2044 - 1005 == 1039, etc.


L = [3123, 1079, 1005, 915, 77]
L_subt = []
x = 0
L_subt.append(x)

for i in range(1, len(L)):
    x -= L[i]
    L_subt.append(x)

print(L_subt)





###Zadanie 2.
#   Z podanej listy do nowej listy przenieś pierwszych sześć słów.
#   Użyj pętli while, ale nie for.

L = [99, 3, 1,1,1, 8, 'Słowianie', [], 'żyli', 'w', [1, [2.78, [[]]]],
    'domach', 'z' , 'drewna', -1000, ((0,1,0),(1,0,0),(1,1,0)),
    ', gdzie', 'gotowali', 'mamałygę',
    {'i spożywali ją bez frasunku, duby smalone plotąc.'}]


L_new = []
i = 0

while len(L_new) < 6 and i < len(L):
    if isinstance(L[i], str):
        L_new.append(L[i])
    i += 1

print(L_new)


## Zadanie 1.
#   Napisz program sumujący elementy listy.
List_0 = list(range(5, 89, 4))
def sum_list_elements(lista):
    sum = 0
    for x in lista:
        sum += x
    print("Suma listy: ", sum)

print(sum_list_elements(List_0))

def sum_list_elements(lista):
    return sum(lista)

print("Suma listy:", sum_list_elements(List_0))




## Zadanie 2.
#   Napisz program wyliczający średnią arytmetyczną danego zestawu danych.

List_1 = [0, 0, 12, 5, 67, 90, 18, 12, 15]

average = sum(List_1) / len(List_1)
print("Średnia arytmetyczna:", average)

# rozwiązanie ekstensywne
# z użyciem innej funkcji
# Jakiej metody możemy użyć, aby skrócić to wyrażenie?



## Zadanie 3.
#   Wyczyść listy.

L1 = ["00_7_00", "00_0.99_00"]
L2 = ["00_44_00", "3333,666_00"]

L1_clean = [el.replace("_", "").replace(".", "") for el in L1]
L2_clean = [el.replace("_", "").replace(",", "") for el in L2]

print("Wyczyszczona lista L1:", L1_clean)
print("Wyczyszczona lista L2:", L2_clean)



## Zadanie 4.
#   Napisz funkcję, które:
#    a. wygenerują ciąg N liczb Fibonacciego, gdzie N to N-ty wyraz ciągu;
def fibonacci_n(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

print("Pierwsze 10 liczb Fibonacciego:", fibonacci_n(10))


#    b. wygenerują ciąg 10 liczb Fibonacciego zaczynających się od
#        określonego argumentem punktu początkowego.
def fibonacci_custom(start, n):
    fib_sequence = [start, start + 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print("10 liczb Fibonacciego od punktu początkowego 5:", fibonacci_custom(5, 10))



## Zadanie z gwiazdką.
#   Wylicz silnię z arbitralnie podanej liczby.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
number = 5
print(f"Silnia z {number} wynosi:", factorial(number))