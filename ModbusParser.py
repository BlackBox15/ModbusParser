# импорт для возможности чтения входящих аргументов
import sys
import crc16

actionToPerform = 0         # Choise from user to perform some action
modbusString = ""           # MODBUS string

print("MODBUS parser")
actionToPerform = int(input("Input a type of data: 1 - pool, 2 - responce\n"))
if actionToPerform in (1, 2):
    print(f"your choise is {actionToPerform}")
    modbusString = input("Input an MODBUS string\n")
    crc16.crc16(modbusString)
else:
    print("Wrong input")

