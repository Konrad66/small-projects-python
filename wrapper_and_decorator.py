# def wrapper_function(func):
#     def wrapped(*args, **kwargs):
#         print("Before the function call")
#         #*args przekazuje argumenty pozycyjne, (tutaj ma znaczenie kolejność, podawanych wartości)
#         #**kwargs przekazuje argumenty poprzez nazwe (tutaj wywołane po nazwie)
#         result = func(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapped
#
# def greet(name, second_name, last_name="Kowalski",age = 18):
#     print(f"Hello, {name}!")
#
# #wrapped_greet = wrapper_function(greet)
# #wrapped_greet("John","Martin",age=20)
#
#
# #jak odpalamy funkcje z dekoratorem, uruchamiany jest dekorator zamiast tej funkcji
# # i przekazywana jest jkako argument właściwa funkcja,
# # następnie uruchamiana jest funkcja zwrócona przez dekoratora z właściwymi argumentami
#
#
#
# def wrapper_function(func):
#     def wrapped(*args, **kwargs):
#         print("Before the function call")
#         result = func(*args, **kwargs)
#         print("After the function call")
#         return result
#     return wrapped
#
# @wrapper_function
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("John")
#


def wrapper_function(func):
    def wrapped(name):  # Przekazujemy tylko argument name
        print("Before the function call")
        result = func(name)  # Wywołujemy func tylko z name
        print("After the function call")
        return result
    return wrapped


def greet(name):
    print(f"Hello, {name}!")

wrapped_greet = wrapper_function(greet)
wrapped_greet("John")



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Przed wykonaniem funkcji")
        result = func(*args, **kwargs)
        print("Po wykonaniu funkcji")
        return result
    return wrapper

@my_decorator
def say_hello(name, surname = "Kowalski", age = 18):
    print(f"Hello, {name}!")
    print(f"{surname}", age)

imie = "John"
say_hello("Johny") # -> **args
say_hello(imie, age = 17) # -> **kwargs



