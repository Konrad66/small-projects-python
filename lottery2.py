import random

USER_NUMBERS_COUNT = 6
NUMBERS_COUNT = 24
guessed_numbers = 0
amount = 0

def fill_user_numbers_list():
    user_numbers_list = []
    while len(user_numbers_list) < USER_NUMBERS_COUNT:
        user_number = int(input("Podaj liczbe: "))
        if 0 >= user_number or user_number > NUMBERS_COUNT:
            print("Liczba ze zlego zakresu")
        elif user_number in user_numbers_list:
            print("Jest juz w zbiorze")
        else:
            user_numbers_list.append(user_number)
    return user_numbers_list

def fill_random_number_set():
    random_number_set = set()
    while len(random_number_set) < 6:
        random_number_set.add(random.randint(1, 24))
    return random_number_set

user_numbers = fill_user_numbers_list()
random_numbers = fill_random_number_set()


user_numbers_set = set(user_numbers)

common_elements = user_numbers_set.intersection(random_numbers)
guessed_numbers = len(common_elements)
print(common_elements)
print(guessed_numbers)

price_dict = {3: 15, 4: 200, 5: 4000, 6: 1500000}

# amount = price_dict[guessed_numbers]
amount = price_dict.get(guessed_numbers, 0)

print(f"Twoja nagroda to {amount} zł")

print(user_numbers)
print(random_numbers)


#TODO dopowiedziec jedna rzecz z funkcji
