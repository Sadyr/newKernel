""" import traceback

def spam():
    bacon()

def bacon():
    raise Exception('Это сообщение об ошибке.')

spam()  """

import traceback


try:
    raise Exception("Это сообщение об ощибке.")
except:
    errorFile = open('errorinfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Информация о стеке вызовой была записана в файл errorinfo.txt')
