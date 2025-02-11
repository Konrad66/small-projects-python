#Wycinek
#wycinki pozwalaja nam z jednej kolekcji wyciąć część elementów i zwróci to do nowej kolekcji, którą możemy
# przypisać do nowej zmiennej

krotka = (3, 9, 27, 81, 243, 729)

#sekwencja[start:stop:step]
#start (opcjonalne): Indeks, od którego zaczyna się wycinek. Domyślnie 0.
#stop (opcjonalne): Indeks, na którym kończy się wycinek (ale nie obejmuje tego indeksu).
#step (opcjonalne): Krok, czyli odstęp między kolejnymi elementami w wycinku. Domyślnie 1.

print(krotka[0:3])
print(krotka[0:10]) # -> nie powoduj to błędu w momencie jezeli podamy za dużo elementów


#możemy sobie trochę namieszać przy tych wycinkach i kazać stworzyć nową kolekcję i liczyć elementy od końca
# w tym przypadku jak liczymy od końca pierwszy element to 1 a nie 0
print(krotka[-4:-2])



# w przypadku wycinków możemy również napisać instrukcję skoku tak jak miało to miejsce w przypadku range,
# czyli co który element będzie nam zapisywać nowe elementy
print(krotka[0:6:2])



# tutaj taka ciekawostka, możemy nie podawać np kiedy ma się zatrzymać i będzie lecieć do końca kolekcji
print(krotka[1::2])


#możemy dzieki temu również odwrócić całą naszą kolekcję stosująć - w instrukcji skoku
print(krotka[:3:-1])
