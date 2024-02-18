import functions2 as fun
from datetime import date
import calendar

today = date.today()
month_num = today.month
month = calendar.month_name[month_num]


print("Witaj w programie, ktory umożliwia śledzenie twoich miesięcznych wydatków!")
print("-------------------------------------------------------------------------------")
print("Jeśli chcesz dodać nowy wydatek wybierz 1.")
print("Jeśli chcesz ustawić limit miesięczny wydanych pieniędzy wybierz 2.")
print(f"Jeśli chcesz sprawdzić ile wydałeś pieniędzy w miesiącu {month} wybierz 3.")
print("Jeśli chcesz sprawdzić ile pieniędzy możesz jeszcze wydać w aktualnym miesiącu wybierz 4.")
print("Jeśli chcesz sprawdzić aktualnie ustawiony limit wybierz 5.")
option = int(input("Wybrany numer: "))

print("--------------------------------------------------------------------------------")

while option < 1 or option > 5:
    print("Wybrany numer powinien być z zakresu 1-5")
    option = int(input("Spróbuj ponownie: "))


while option < 6:

    match option:
        case 1:
            fun.add()
        case 2:
            fun.set_limit()
        case 3:
            fun.get_exp()
        case 4:
            fun.check_limit()
        case 5:
            fun.get_limit()

    print("-------------------------------------------------------------------------------")
    print("Jeśli chcesz dalej korzystać z programu, podaj nowy numer.")
    print("Jeśli chcesz zakończyć działanie programu, podaj dowolny numer większy niż 5 ")
    option = int(input("Wybrany numer: "))
    print("--------------------------------------------------------------------------------")


print("Koniec działania programu")