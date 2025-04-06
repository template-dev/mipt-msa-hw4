from abc import ABC, abstractmethod
import requests, json, time, os, logging

class BaseCurrencyConverter(ABC):
    def __init__(self, api_url="https://api.exchangerate-api.com/v4/latest/USD", cache_file="exchange_rates.json", cache_expiry=3600):
        self.api_url = api_url
        self.cache_file = cache_file
        self.cache_expiry = cache_expiry
        self.logger = self._setup_logger()
        self.rates = self.get_rates()

    def _setup_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        return logger

    def _load_from_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    data = json.load(f)
                    if time.time() - data['timestamp'] < self.cache_expiry:
                        return data['rates']
            except (json.JSONDecodeError, KeyError):
                self.logger.warning("Invalid cache. Fetching from API.")
        return None

    def _save_to_cache(self, rates):
        try:
            with open(self.cache_file, 'w') as f:
                json.dump({'timestamp': time.time(), 'rates': rates}, f)
        except IOError as e:
            self.logger.error(f"Error saving to cache: {e}")

    def get_rates(self):
        rates = self._load_from_cache()
        if rates:
            return rates

        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            rates = data['rates']
            self._save_to_cache(rates)
            return rates
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            self.logger.error(f"Error fetching exchange rates: {e}")
            return {}

    @abstractmethod
    def convert(self, amount: float) -> float:
        pass
