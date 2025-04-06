from converters import UsdRubConverter, UsdEurConverter, UsdGbpConverter, UsdCnyConverter

def main():
    try:
        amount = float(input('Введите сумму в USD: '))
    except ValueError:
        print("Ошибка: Введите корректное число.")
        return

    converters = {
        'RUB': UsdRubConverter(),
        'EUR': UsdEurConverter(),
        'GBP': UsdGbpConverter(),
        'CNY': UsdCnyConverter()
    }

    for currency, converter in converters.items():
        result = converter.convert(amount)
        print(f"{amount} USD to {currency}: {result:.2f}")

if __name__ == "__main__":
    main()