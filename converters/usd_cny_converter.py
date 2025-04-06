from converters.currency_converter import BaseCurrencyConverter

class UsdCnyConverter(BaseCurrencyConverter):
    def convert(self, amount: float) -> float:
        return amount * self.rates.get('CNY', 0.0)