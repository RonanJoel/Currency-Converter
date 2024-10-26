from converter import CurrencyConverter

def main():
    converter = CurrencyConverter()
    rates = converter.get_rates()

    if rates is None:
        print("Could not retrieve exchange rates.")
        return

    print("Available exchange rates:")
    for currency in rates.keys():
        print(currency)

    from_currency = input("Enter the currency to convert from (e.g., USD): ")
    to_currency = input("Enter the currency to convert to (e.g., EUR): ")
    amount = float(input("Enter the amount to convert: "))

    result = converter.convert(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is equivalent to {result:.2f} {to_currency}")
    else:
        print("Invalid conversion.")

if __name__ == "__main__":
    main()


