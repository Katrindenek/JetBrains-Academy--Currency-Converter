import requests


def get_url(a_curr_code):
    return f"http://www.floatrates.com/daily/{a_curr_code}.json"


def get_exchange_rate(from_currency, to_currency):
    url = get_url(from_currency)
    response_json = requests.get(url).json()

    exchange_rate = response_json[to_currency]['rate']
    return exchange_rate


def add_to_cache(from_currency, to_currency):
    if from_currency != to_currency:
        cache[to_currency] = get_exchange_rate(from_currency, to_currency)
    else:
        cache[to_currency] = 1


def converter(from_currency, to_currency, money):
    print("Checking the cache...")
    if to_currency in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        add_to_cache(from_currency, to_currency)

    exchange_rate = cache[to_currency]
    converted_money = money * exchange_rate
    print(f"You received {converted_money:.2f} {to_currency.upper()}.")


def main():
    print('Welcome to Currency Converter!')
    print('Please, enter Currency Codes to proceed:')
    currency_code_from = input('From: ').lower()
    add_to_cache(currency_code_from, usd)
    add_to_cache(currency_code_from, eur)
    while True:
        currency_code_to = input('To: ').lower()
        if not currency_code_to:
            break
        money_amount = float(input('Amount of money: '))
        converter(currency_code_from, currency_code_to, money_amount)


cache = dict()
usd, eur = 'usd', 'eur'
if __name__ == '__main__':
    main()
