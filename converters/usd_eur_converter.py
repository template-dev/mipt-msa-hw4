from converters.currency_converter import BaseCurrencyConverter

class UsdEurConverter(BaseCurrencyConverter):
    def convert(self, amount: float) -> float:
        return amount * self.rates.get('EUR', 0.0)