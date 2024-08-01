import random
import matplotlib.pyplot as plt


def die():
    return random.randint(1, 6)


def rollaPair():
    return die(), die()


def graphRolls(qty, rollValues):
    maxnum = qty
    coder = input("Who am I working with? ")
    num_bins = 11
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(rollValues,num_bins)
    plt.title(f"Random Dice Rolls for {maxnum} Times done by {coder}")
    plt.xlabel("Dice Pair Values ")
    plt.ylabel("Frequency ")
    plt.show()


def main():
    rolls = []
    qty = int(input("how many rolls do you want? "))
    for c in range(qty):
        die1, die2 = rollaPair()
        mysum = die2 + die1
        rolls.append(mysum)
    print(rolls)
    graphRolls(qty, rolls)

main()
