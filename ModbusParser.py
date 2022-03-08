# импорт для возможности чтения входящих аргументов
import sys
##import crc16
import HelpPage
##-------------------------------------------------
modbusString = ""           # MODBUS string
##-------------------------------------------------
print("\n", "." * 10, "MODBUS parser", "." * 10, "\n")

if (sys.argv[1]) == '-h':
    # выводим страницу помощи
    HelpPage.printHelpPage()
elif (sys.argv[1]) == '-p':
    # расшифровываем как Pool
    print("Decode as Pool..")
elif (sys.argv[1]) == '-r':
    # расшифровываем как Request
    print("Decode as Request..")
else:
    # выводим сообщение, что входные данные ошибочны
    print("Unknown arguments.")
    print("Use -h for help.")
      
### Список входящих аргументов.
##args = sys.argv[:]
##
####print("Количество входящих аргументов: {0}".format(len(sys.argv[])))
##print("Количество входящих аргументов")
##print(len(sys.argv))
##print(sys.argv)

##for i in args:
##    print(i)

##HelpPage.printHelpPage()



    
####    Запрос Modbus-строки
##modbusString = input("Input an MODBUS string\n")
##
####  Вывод Modbus-строки
##print("{0:x}".format(crc16.crc16(modbusString)))

##actionToPerform = int(input("Input a type of data: 1 - pool, 2 - responce\n"))

##if actionToPerform in (1, 2):
##    print(f"your choise is {actionToPerform}")
##    

##else:
##    print("Wrong input")
##
##
####-------------------------------------------------
####Тестирование работы с переменными типа Bytes.
####-------------------------------------------------
####Передаём значение, заведомо большее, чем 1 байт...
##bytesTest = bytes.fromhex("ffffff")
##
##print(type(bytesTest))
##print(f"Lenght of array = {len(bytesTest)}")
##print(f"Байты в переменной bytesTest: {bytesTest}")
##
##for b in bytesTest:
##    print(b)
##
##bytesToJoin = bytes.fromhex("ff")
##bytesTest += bytesToJoin;
##bytesArray = bytearray([df, a1])
##bytesTest.join(bytesArray)
##
##print(f"Lenght of array = {len(bytesTest)}")
##print(f"Байты в переменной bytesTest: {bytesTest}")
##
##for b in bytesTest:
##    print(b)
