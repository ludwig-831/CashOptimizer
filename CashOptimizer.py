def get_optimal(price, cash_avail_int, cash_avail_string):
    """ Takes a price and optimally breaks it down into the cah units of the
    given currency. Returns a list of strings to be printed.
    """
    price *= 100 # convert price to cents
    price = round(price) # make price an integer

    for i in range(len(cash_avail_int)):
        amount = price//cash_avail_int[i] # optimal number of notes/coins for this unit of cash
        cash_avail_string[i] += ": {}".format(amount) # append to the string list so
        # for "pretty" printing
        price -= amount*cash_avail_int[i] # subtract the money that is already
        # accounted for with the units of cash that were checked so far

    return cash_avail_string

# INPUTS FOR EUR (€)
cash_avail_string_EUR = ["500 €",
        "200 €",
        "100 €",
        "50 €",
        "20 €",
        "10 €",
        "5 €",
        "2 €",
        "1 €",
        "50 ct",
        "20 ct",
        "10 ct",
        "5 ct",
        "2 ct",
        "1 ct"]

cash_avail_int_EUR = [# cash units in cents
        500*100,
        200*100,
        100*100,
        50*100,
        20*100,
        10*100,
        5*100,
        2*100,
        1*100,
        50,
        20,
        10,
        5,
        2,
        1]

# INPUTS FOR USD ($)
cash_avail_string_USD = [
        "100 $",
        "50 $",
        "20 $",
        "10 $",
        "5 $",
        "2 $",
        "1 $",
        "25 ct",
        "10 ct",
        "5 ct",
        "1 ct"]

cash_avail_int_USD = [# cash units in cents
        100*100,
        50*100,
        20*100,
        10*100,
        5*100,
        2*100,
        1*100,
        25,
        10,
        5,
        1]


# Showcase
price = 80685.99
print(get_optimal(price, cash_avail_int_EUR, cash_avail_string_EUR))
print(get_optimal(price, cash_avail_int_USD, cash_avail_string_USD))
