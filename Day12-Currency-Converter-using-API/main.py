import os
import time
import datetime
import requests
from dotenv import load_dotenv
from cachier import cachier
from babel import numbers as babel_numbers
import logging

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

VALID_CURRENCIES = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP",
    "CNH", "CNY", "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP",
    "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL",
    "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK",
    "HTG", "HUF", "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP",
    "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD",
    "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL",
    "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN",
    "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB",
    "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB",
    "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL",
    "SOS", "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND",
    "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU",
    "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XCG", "XDR", "XOF",
    "XPF", "YER", "ZAR", "ZMW", "ZWG", "ZWL"
]

SEPARATOR = "=" * 50

logging.basicConfig(format="%(message)s", level=logging.DEBUG)

if not API_KEY:
    raise ValueError("EXCHANGE_API_KEY environment variable not set!")

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"


@cachier(stale_after=datetime.timedelta(days=1))
def get_exchange_data(base_currency):
    url = BASE_URL + base_currency
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("result") == "success":
                logging.info("Fresh data fetched from API")
                data["_fetched_at"] = time.time()
                return data
            else:
                logging.error(f"API Error: {data.get('error-type')}")
        else:
            logging.error(f"HTTP Error: Status Code {response.status_code}")
    except requests.RequestException as e:
        logging.error(f"Network Error: {e}")

    return None


def get_valid_currency(prompt):
    while True:
        user_input = input(prompt).upper().strip()

        if not user_input.isalpha() or len(user_input) != 3:
            logging.error("Error: Currency code must be 3 letters (e.g., USD).")
            continue

        if user_input not in VALID_CURRENCIES:
            logging.error(
                f"Warning: '{user_input}' might not be supported or is invalid."
            )
            continue

        return user_input


def get_valid_amount(currency_name):
    while True:
        user_input = input(f"Enter {currency_name} amount: ").strip()
        try:
            val = float(user_input)
            if val < 0:
                logging.error("Error: Amount cannot be negative.")
                continue
            return val
        except ValueError:
            logging.error("Error: Please enter a valid numeric amount.")


def convert_currency(base_currency, target_currency, amount):
    data = get_exchange_data(base_currency)

    if not data:
        return None

    rates = data.get("conversion_rates", {})
    rate = rates.get(target_currency)

    if not rate:
        logging.error(f"Currency {target_currency} not found")
        return None

    exchange_amount = amount * rate

    fetch_time = data.get("_fetched_at", 0)
    is_cached = (time.time() - fetch_time) > 2

    return {
        "amount": exchange_amount,
        "rate": rate,
        "timestamp": data.get("time_last_update_utc"),
        "from_cache": is_cached,
    }


def get_currency_symbol_name(currency):
    name = babel_numbers.get_currency_name(currency, locale="en_US")
    sym = babel_numbers.get_currency_symbol(currency, locale="en_US")
    return sym, name


def currency_convertor():
    logging.info(f"\n{SEPARATOR}\n {'Currency Converter':^50}\n{SEPARATOR}")
    base_currency = get_valid_currency("Enter Base Currency (e.g., USD): ")
    while True:
        target_currency = get_valid_currency("Enter Target Currency (e.g., EUR): ")
        if target_currency == base_currency:
            logging.error(
                f"Your target currency cannot match with your base currency {base_currency}"
            )
            continue
        break

    amount = get_valid_amount(base_currency)

    b_sym, b_name = get_currency_symbol_name(base_currency)
    t_sym, t_name = get_currency_symbol_name(target_currency)

    result = convert_currency(base_currency, target_currency, amount)

    logging.info(f"{SEPARATOR}")
    if result:
        output_lines = [f"{key}: {value}" for key, value in result.items()]
        return (
            f"Base Currency: {b_name}\n"
            f"Input Amount: {b_sym} {amount:,.2f}\n"
            f"{SEPARATOR}\n"
            f"Target Currency: {t_name}\n"
            f"Converted Amount: {t_sym} {result['amount']:,.2f}\n"
            f"{SEPARATOR}\n"
            f"Data Dump:\n" + " \n".join(output_lines)
        )

    return "Conversion failed. Please check your currency codes or API key."


if __name__ == "__main__":
    logging.info(currency_convertor())
