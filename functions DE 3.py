
currency_from = input("Please enter a currency you would to convert from: e.g. £ $ € ")
currency_to = input("Please enter a currency you would to convert to: e.g. £ $ € ")
amount = int(input("Please enter the amount you would like converted: "))



def pounds_dollar(currency_from,currency_to,amount):
    total = amount * 1.601
    print("$",total)

def pounds_euro(currency_from,currency_to,amount):
    total = amount * 1.229
    print("€",total)

def euro_pounds(currency_from,currency_to,amount):
    total = amount * 0.814
    print("£",total)

def euro_dollar(currency_from,currency_to,amount):
    total = amount * 1.302
    print("$",total)

def dollar_pound(currency_from,currency_to,amount):
    total = amount * 0.625
    print("£",total)

def dollar_euro(currency_from,currency_to,amount):
    total = amount * 0.768
    print("€",total)


#main program

if currency_from == "£":
    if currency_to == "$":
        pounds_dollar(currency_from,currency_to,amount)
    elif currency_to == "€":
        pounds_euro(currency_from,currency_to,amount)
    else:
        print("One of the values you have entered is invalid")

elif currency_from == "€":
    if currency_to == "£":
        euro_pounds(currency_from,currency_to,amount)
    elif currency_to == "$":
        euro_dollar(currency_from,currency_to,amount)
    else:
        print("One of the values you have entered is invalid")

elif currency_from == "$":
    if currency_to == "£":
        dollar_pound(currency_from,currency_to,amount)
    elif currency_to == "€":
        dollar_euro(currency_from,currency_to,amount)
    else:
        print("One of the values you have entered is invalid")


else:
    print("One of the values you have entered is invalid")
