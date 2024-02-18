with open('expenses.txt', 'r') as exp:
    e = exp.read()
    var = int(e)

amount = int(input("Podaj kwote:"))
money = str(var + amount)

with open('expenses.txt', 'w') as exp:
    exp.write(money)