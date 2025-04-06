from converters.currency_converter import BaseCurrencyConverter

class UsdRubConverter(BaseCurrencyConverter):
    def convert(self, amount: float) -> float:
        return amount * self.rates.get('RUB', 0.0)