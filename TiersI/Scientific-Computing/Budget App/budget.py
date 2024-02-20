class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.ledgerDic = {}
        self.money = 0

    def deposit(self, a, *description):
        self.money += a
        try:
            self.ledger.append({"amount": a, "description": description[0]})
        except IndexError:
            self.ledger.append({"amount": a, "description": ""})

    def check_funds(self, b):
        return self.money - b >= 0

    def withdraw(self, a, *description):
        if self.check_funds(a) is True:
            self.money -= a
            try:
                self.ledger.append({"amount": -abs(a), "description": description[0]})
            except IndexError:
                self.ledger.append({"amount": -abs(a), "description": ""})
            return True
        else:
            return False

    def transfer(self, x, to):
        if self.check_funds(x) is True:
            self.money -= x
            self.ledger.append(
                {"amount": -abs(x), "description": ("Transfer to " + to.name)}
            )
            to.money += x
            to.ledger.append(
                {"amount": x, "description": ("Transfer from " + self.name)}
            )
            return True
        else:
            return False

    def get_balance(self):
        return self.money

    def __str__(self) -> str:
        spacer = ""
        for i in range(int((30 - len(self.name)) / 2)):
            spacer += "*"
        firstLine = spacer + self.name + spacer + "\n"
        secondLine = ""
        for i in range(len(self.ledger)):
            secondLine += (
                str(self.ledger[i]["description"])[:23]
                + " "
                + "{:>{y}.2f}".format(
                    self.ledger[i]["amount"],
                    y=29 - len(str(self.ledger[i]["description"])[:23]),
                )
                + "\n"
            )
        lastLine = "Total: " + str(self.money)
        return firstLine + secondLine + lastLine


def create_spend_chart(categories):
    spendByCat = []
    spendByCatP = []
    totalspend = 0
    catNameMaxLen = 0
    divider = ""

    # Getting the Percentage Spent
    for i in range(len(categories)):
        # Getting the max len of name & creating the divider
        divider += "---"
        if len(categories[i].name) > catNameMaxLen:
            catNameMaxLen = len(categories[i].name)
        # Getting the total spent & for each cat
        tempSpend = 0
        for x in range(len(categories[i].ledger)):
            if categories[i].ledger[x]["amount"] < 0:
                tempSpend += categories[i].ledger[x]["amount"]
        spendByCat.append(tempSpend)
        totalspend += tempSpend
    # Getting the pourcentage spend by cat
    for i in range(len(spendByCat)):
        spendByCatP.append(int(spendByCat[i] / totalspend * 100))

    # Creating the string chart
    spendChart = "Percentage spent by category\n"

    # Printing each % line and checking if an cat is inside of it.
    temp100 = 100
    for i in range(11):
        spendChart += "{:>3}".format(temp100) + "|"
        for x in range(len(spendByCatP)):
            if spendByCatP[x] >= temp100:
                spendChart += " o "
            else:
                spendChart += "   "
        spendChart += " \n"
        temp100 -= 10

    # formating & adding the divider
    spendChart += "{:>{x}}".format(divider, x=4 + len(divider)) + "-\n"

    # Printing each Line with a character of the cat name
    for i in range(catNameMaxLen):
        spendChart += "    "
        for x in range(len(categories)):
            if categories[x].name[i : i + 1] == "":
                spendChart += "   "
            else:
                spendChart += " " + categories[x].name[i : i + 1] + " "
        spendChart += " \n"
    return spendChart[:-1]
