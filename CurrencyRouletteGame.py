import requests
import json

def get_money_interval(difficulty , currency_rate, amount):
    d = int(difficulty)
    match d:
        # pattern 1
        case 1:
            d = int(5)
        # pattern 2
        case 2:
            d = int(4)
        # pattern 3
        case 3:
            d = int(3)
        # pattern 4
        case 4:
            d = int(2)
        # pattern 5
        case 5:
            d = int(1)
    print(d)

    print(amount)
    l = float((currency_rate - (5 - d)))
    h = float((currency_rate + (5 - d)))
    print(l)
    print(h)
    #print(currency_rate)
    total_value_of_money = (((currency_rate - (5 - d)) * amount), ((currency_rate + (5 - d)) * amount))
    return total_value_of_money
def get_guess_from_user(total_value_of_money,currency_rate,name, date):
    print("\n\n\n\n\n\n\n\nILS current exchange rate: ", currency_rate)
    print("Rate vaildate date: ", date)
    print("Total range money value: ",total_value_of_money)
    print(name)
    user_guess = int(input("Please guess the value to a given amount of USD amount for the ILS we exchanged: "))
    return user_guess

def compare_results(user_guess, amount):
    if amount == user_guess:
        return True
    else:
        return False
def play(difficulty, name):
    import random
    amount = random.randint(1, 100)
    #print(amount)

    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/2bf8e1d422858b2f3e4710e9/latest/USD'

    # Making our request
    response = requests.get(url)
    data = response.json()

    # the result is a JSON string:
    date = (json.dumps(data['time_last_update_utc'], indent=4, sort_keys=True))
    USD = float(json.dumps(data['conversion_rates']['USD']))
    #print("Total USD: ", USD)
    # print(json.dumps(data['conversion_rates']['USD'], indent = 4, sort_keys=True))
    ILS = float(json.dumps(data['conversion_rates']['ILS']))
    #print("Total ILS: ", ILS)
    # print(json.dumps(data['conversion_rates']['ILS'], indent = 4, sort_keys=True)

    total_value_of_money = get_money_interval(difficulty, ILS, amount)
    user_guess = get_guess_from_user(total_value_of_money,ILS,name,date)
    results = bool(compare_results(user_guess, amount))
    print(results)
    if results == True:
        print("\n\n\n", name, "You have Won !!!!!!! the USD amount we exchanged is: ", amount , "$")
    else:
        print("\n\n\n", name, "You have Lost !!!!!!! the USD amount we exchanged is: ", amount, "$")