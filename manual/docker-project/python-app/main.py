import calendar

print('Добро пожаловать в супер  календарь \n')


year = int(input('Пожалуйста введите год '))
month = int(input('Введите номер месяца: '))

print(calendar.month(year,month))

print("Всего хорошего! ")
