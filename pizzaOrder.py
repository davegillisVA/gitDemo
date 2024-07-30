

def pizzaOrder(*argpizza, wings = 0, drinks = [], coupons = 0):
    finaltotal = 0
    wingsP = {10: 5, 20: 9, 40: 17.50, 100: 48}
    drinksP = {'s': 2, 'm': 3, 'l': 3.75, 'tub': 4.25}
    toppingP = {'peperoni': 2, 'mushrooms': 0.75, 'olives': 0.75, 'anchovies': 2.25}
    total = 0
    pizzaP = 13
    if wings != 0:
        total += wingsP[wings]
    for eachdrink in drinks:
        total += drinksP[eachdrink]
    for eachpizza in argpizza:
        total += pizzaP
        for eachtopping in eachpizza:
            if eachtopping in toppingP:
                total += toppingP[eachtopping]
            else:
                print("Sorry we do not offer ",eachtopping," as a topping.")
    if coupons != 0:
        discTotal = total*(1-coupons)
    else:
        discTotal = total
    tax = total*0.065
    finaltotal = discTotal + tax
    print("The total cost for the order is: ",'${:0,.2f}'.format(finaltotal))

    print(total)













def main():

    pizzaOrder([],[],['mushroom'],['ham','olives'], ['peperoni'], [], wings=100, drinks=[], coupons=.10)


main()