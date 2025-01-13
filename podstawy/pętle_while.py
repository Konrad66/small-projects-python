# pętle while służą do zapętlania i wykonywania czegoś wielokrotnie

# pętla while to rodzaj pętli prymitywnej

# tworząc pętle while
# trzeba uważać aby nie stworzyć pętli nieskończonej czyli takiej która będzie się tworzyć w nieskończoność

# while możemy sobie przetłumaczyć jako dopóki,
# czyli dopóki nasz warunek po prawej stonie będzie prawdziwy to wykonuj segment kodu

i = 0

while i < 5:
    print(i)
    i += 1

# w tym przypadku patrząć na pętle możemy zobaczyć,
# że pętla wydaje się nieskończona możemy mimo wszystko ją zakończyć dzięki poleceniu break

while True:
    print(i)
    i += 1
    if i >= 5:
        break


#o co chodzi w tym przykładzie - dzięki słówku continue
#możemy pominąć wszystkie linie kodu poniżej tego słówka i wyświetlić to co nas interesuje
while True:
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break
print("Koniec")


#instrukcje break i continue nazywami instrukcjami skoku bo one gdzieś przeskakują