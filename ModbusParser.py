# импорт для возможности чтения входящих аргументов
import sys
import crc16
##-------------------------------------------------
actionToPerform = 0         # Choise from user to perform some action
modbusString = ""           # MODBUS string
##-------------------------------------------------
print("\n", "." * 10, "MODBUS parser", "." * 10, "\n")


##    Запрос Modbus-строки
modbusString = input("Input an MODBUS string\n")

print("{0:x}".format(crc16.crc16(modbusString)))

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
