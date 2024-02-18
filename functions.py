from datetime import date

exp = open("expenses.txt", 'a')
exp2 = open("expenses2.txt", 'a+')
exp3 = open("expenses.txt", 'r')
lim = open("limit.txt", 'w')
mnt = open("month.txt", 'w+')
now = date.today()


def add():
    amount = input("Podaj kwote:")
    exp.write(amount)
    response = input("Czy chcesz dodac dodtkowe informacje na temat wydatku? ")
    if response == 'tak':
        add2(amount)


def add2(amount):
    item = input("Co kupiles?")
    data = input("Kiedy?")
    info = f"{item}, {amount} pln, {data}"
    exp2.write(info)


def remove_exp():  # wykonuje sie bez wiedzy uzytkownika i usuwa zawartosc plikow z wydatkami
    day = now.day

    if day == 1:
        exp.write("0")


def get_exp():  # sprawdzanie sumy wydatkow w miesiacu
    e = exp3.read()
    return e


def check_limit():  # sprawdzanie ile limitu zostalo
   print("Limit wynosi: ")


def set_limit():
    limit = input('Jaką kwote chcesz wydac w tym miesiacu? ')
    lim.write(limit)

def get_limit():
    pass


def limit_info():
    print("info")


