def say_hello(name, surname="Kowalski", age=18):
    if len(name) > 0:
        return f"Hello {name} {surname} {age}"


print(say_hello("Konrad", age=26))
print(say_hello("Wiktor"))
