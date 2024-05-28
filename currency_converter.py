import requests

def get_exchange_rate(api_key, from_currency, to_currency):
    """
    Get the exchange rate from one currency to another using a free exchange rate API.

    Parameters:
    api_key (str): Your API key for the exchange rate service.
    from_currency (str): The base currency code (e.g., 'USD').
    to_currency (str): The target currency code (e.g., 'EUR').

    Returns:
    float: The exchange rate from the base currency to the target currency.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def convert_currency(amount, exchange_rate):
    """
    Convert an amount of money using a given exchange rate.

    Parameters:
    amount (float): The amount of money to convert.
    exchange_rate (float): The exchange rate to use for the conversion.

    Returns:
    float: The converted amount of money.
    """
    return amount * exchange_rate

if __name__ == "__main__":
    # Example usage
    api_key = "your_api_key"  # Replace with your actual API key
    from_currency = "USD"
    to_currency = "EUR"
    amount = 100  # Amount in the base currency

    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
    converted_amount = convert_currency(amount, exchange_rate)

    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
