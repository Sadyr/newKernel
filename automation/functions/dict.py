birthdays = {'ALisa':'apr 1', 'Bob':'dec 12',  'Carol':'Marth 5'}


while True:
    print('Enter name (<Enter> for exit):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + ': birhday - ' + birthdays[name])
    else:
        print('I dont know when birthday that ' + name)
        print('When birthday  that person?')
        bday = input()
        birthdays[name]=bday
        print("Update information about birthdays")

