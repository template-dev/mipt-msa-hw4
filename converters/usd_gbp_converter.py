from converters.currency_converter import BaseCurrencyConverter

class UsdGbpConverter(BaseCurrencyConverter):
    def convert(self, amount: float) -> float:
        return amount * self.rates.get('GBP', 0.0)