def tax_decorator(func):
    def wrapper(*args, **kwargs):
        base = func(*args, **kwargs)
        taxable_amount = args[0]
        if taxable_amount <= 120_000:
            # I próg: 12% minus 3600 zł
            tax = base - 3600
        else:
            # II próg: 32% dla nadwyżki ponad 120,000 PLN + 10,800 zł
            excess = taxable_amount - 120_000  # Kwota powyżej progu
            tax = (120_000 * 12 / 100) + (excess * 32 / 100) + 10_800
        return tax
    return wrapper


# użycie adnotacji @tax_decorator - pozwala na szybsze użycie dekoratora, nie trzeba jej dodatkowo używać
@tax_decorator
def tax(taxable_amount, rate=20):
    return taxable_amount * rate / 100  # Bazowa funkcja, której nie zmieniamy


# rate -> % opodatkowania
# func = tax_decorator(tax)

# Przykładowe wywołania
print(tax(110_000, 12))  # Kwota poniżej progu, powinien naliczyć I próg  -> 8_400
print(tax(150_000, 32))  # Kwota powyżej progu, powinien naliczyć II próg -> 34_800