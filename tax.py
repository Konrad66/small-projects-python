def tax_decorator(func):
    def wrapper(taxable_amount, rate):
        tax_threshold = 120_000  # granica progu podatkowego
        # wyciągnięcie do zmiennej podstawowego liczenia podatku
        base_tax = func(taxable_amount, rate)

        if taxable_amount <= tax_threshold:
            tax = base_tax - 3600
        else:
            excess = taxable_amount - tax_threshold
            tax_first_bracket = func(tax_threshold, rate=12)
            tax_second_bracket = func(excess, rate)
            tax = (tax_second_bracket + 10_800) + (tax_first_bracket - 3600)
        return tax
    return wrapper

@tax_decorator
def tax(taxable_amount, rate=20):
    return taxable_amount * rate / 100

print(tax(110_000, 12))
print(tax(150_000, 32))