import random


number_count = 6
set_number = 24
congratulations = "Udało Ci się wylosować wszystkie 6 cyfr."
# print("Witaj w loteri.", "Wprowadzisz 6 liczb z zakresu od 1-24.", "Zobaczymy ile uda Ci się odgadnąć",sep=" ", end=" ")
# print("Witaj w loteri. Wprowadzisz " + str(number_count) + " liczb z zakresu od 1-" + str(set_number) + ". Zobaczymy ile uda Ci się odgadnąć")
# print("Witaj w loteri. Wprowadzisz " + str(number_count) + " liczb z zakresu od 1-" + str(set_number) + ". Zobaczymy ile uda Ci się odgadnąć")
print("Witaj w loteri", f"Wprowadzisz {str(number_count)} liczb z zakresu od 1-{str(set_number)}.",
      "Zobaczymy ile uda Ci się odgadnąć", sep="\n")

print(f"Wygrałeś!  {congratulations}")

"""
print(type(congratulations))
print(type(set_number))
"""
# [] - to jest lista
# {} - słownik (mapa)
# () - tuple (krotki)

# w pythonie 2 rodzaje pentli while i for

# while len(user_numbers_list) < 6:
#     print("Podaj liczbe: ")
#     user_number = int(input())
#     user_numbers_list.append(user_number)

# for element in sekwencja:
# for i in [0,1,2]:
#   print(i)


# for char in "0, 1, 2":
#       print(char)


# for number in user_numbers_list:
#     print(number)


# for i in range(6):
#     user_number = int(input("Podaj liczbe: "))
#     if 0 >= user_number or user_number > 24:
#         print("Liczba ze zlego zakresu")
#     elif user_number in user_numbers_list:
#         print("Jest juz w zbiorze")
#     else:
#         user_numbers_list.append(user_number)

# numbers_list = list(range(0,25))
# print(numbers_list[-6:-3])

# for user_number in user_numbers_list:
#     for random_number in random_number_set:
#         if user_number == random_number:
#             guessed_numbers += 1




a = input("Podaj 1 liczbe: ")
b = input("Podaj 2 liczbe: ")
print(int(a) + int(b))