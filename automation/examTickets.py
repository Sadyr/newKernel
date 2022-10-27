import random

# Создать 35 различных билетов
# Создать 50 вопросов с множественным выбором для каждого билета, расположив их в случайном порядке
# Предоставить правильный ответ и три случайно выбранных неправильных ответа на каждый вопросы, распологая их в случайном порядке
# Записать билеты в 35 текстовых файлов

# Это значит код должен выполнить следующие операции:
# Вызывать методы open(),write() и close() для текстовых файлов, в которых хранится билеты и ключи ответов
# Использовать функцию random.shuffle() для рандомизации(расположения в случайно порядке следования) вопросов и вариантов множественного выбора

capitals = {'Alabama': 'Montgomery',
              'Alaska': 'Juneau',
              'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock',
              'California': 'Sacramento',
              'Colorado': 'Denver',
              'Connecticut': 'Hartford',
              'Delaware': 'Dover',
              'Florida': 'Tallahassee',
              'Georgia': 'Atlanta',
              'Hawaii': 'Honolulu',
              'Idaho': 'Boise',
              'Illinois': 'Springfield',
              'Indiana': 'Indianapolis',
              'Iowa': 'Des Moines',
              'Kansas': 'Topeka',
              'Kentucky': 'Frankfort',
              'Louisiana': 'Baton Rouge',
              'Maine': 'Augusta',
              'Maryland': 'Annapolis',
              'Massachusetts': 'Boston',
              'Michigan': 'Lansing',
              'Minnesota': 'Saint Paul',
              'Mississippi': 'Jackson',
              'Missouri': 'Jefferson City',
              'Montana': 'Helena',
              'Nebraska': 'Lincoln',
              'Nevada': 'Carson City',
              'New Hampshire': 'Concord',
              'New Jersey': 'Trenton',
              'New Mexico': 'Santa Fe',
              'New York': 'Albany',
              'North Carolina': 'Raleigh',
              'North Dakota': 'Bismarck',
              'Ohio': 'Columbus',
              'Oklahoma': 'Oklahoma City',
              'Oregon': 'Salem',
              'Pennsylvania': 'Harrisburg',
              'Rhode Island': 'Providence',
              'South Carolina': 'Columbia',
              'South Dakota': 'Pierre',
              'Tennessee': 'Nashville',
              'Texas': 'Austin',
              'Utah': 'Salt Lake City',
              'Vermont': 'Montpelier',
              'Virginia': 'Richmond',
              'Washington': 'Olympia',
              'West Virginia': 'Charleston',
              'Wisconsin': 'Madison',
              'Wyoming': 'Cheyenne'}
""" quizFile = []
answerKeyFile = [] """
for num in range(35):
    # Создание файлов билетов и ключей ответов
    quizFile = open(f'capitalquiz{num+1}.txt','w')
    answerKeyFile = open(f'answerKeyFile{num+1}.txt','w')
    # Запись заголовка билета
    quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quizFile.write((' ' * 15 ) + f'Проверка знания столиц шатов (Билет {num+1}) ')
    quizFile.write('\n\n')
    states = list(capitals.keys())
    random.shuffle(states)
    # Организация цикла по всем 50 штатам
# с созданием вопроса для каждого из них.
    for questionNum in range(50):
        # Получение правильных и неправильных ответов
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile.write(f'{questionNum + 1}. Выберите столицу штата {states[questionNum]}\n')
        for i in range(4):
            quizFile.write(f'{"ABCD"[i]}. {answerOptions[i]}\n')
            quizFile.write('\n')
        answerKeyFile.write(f'{questionNum + 1}.{"ABCD"[answerOptions.index(correctAnswer)]}\n')
quizFile.close()
answerKeyFile.close()







