def add():
    with open('expenses.txt', 'r') as exp:
        e = exp.read()
        var = int(e)

    amount = int(input("Podaj kwote:"))
    money = str(var + amount)

    with open('expenses.txt', 'w') as exp:
        exp.write(money)

    response = input("Czy chcesz dodac dodtkowe informacje na temat wydatku? ")
    if response == 'tak':
        add2(amount)


def add2(amount):
    item = input("Co kupiles?")
    data = input("Kiedy?")
    info = f"{item}, {amount} pln, {data}"
    with open('expenses2.txt', 'a') as exp2:
        exp2.write(info)


def get_exp():  # sprawdzanie sumy wydatkow w miesiacu7
    with open('expenses.txt', 'r') as exp:
        e = exp.read()
    print(f"Wydano {e} pln")


def check_limit():  # sprawdzanie ile limitu zostalo
    with open('limit.txt', 'r') as lim:
        limit = lim.read()

    with open('expenses.txt', 'r') as exp:
        expenses = exp.read()

    rest = int(limit) - int(expenses)
    print(f'W tym miesiącu możeszz jeszcze wydać {rest} pln.')


def set_limit():  # ustawianie limitu
    limit = input('Jaką kwote chcesz wydac w tym miesiacu? ')

    with open('limit.txt', 'w') as lim:
        lim.write(limit)


def get_limit():  # sprawdzanie limitu ustawionego w bieżącym miesiącu
    with open('limit.txt', 'r') as lim:
        limit = lim.read()

    print(f"Aktualnie limit wynosi {limit} pln")
