# импорт для возможности чтения входящих аргументов
import sys
import crc16
import HelpPage
##-------------------------------------------------
## Тестовая строка
## -r "01 03 d7 f3 32 78 1a"    CRC isn't correct
## -r "01 03 d7 f3 32 99 6c"    CRC is correct
##-------------------------------------------------
##print("\n", "." * 10, "MODBUS parser", "." * 10, "\n")

if (len(sys.argv) > 0):
    # Случай, когда есть аргументы в командной строке.
    if (sys.argv[1] != '-p') and (sys.argv[1] != '-r') :
        # Выводим страницу помощи.
        HelpPage.printHelpPage()
    elif (sys.argv[2] != ''):
        # У нас команда или -r, или -p.
        # Наличие Modbus-строки в аргументе командной строки.
        # Вычисляем CRC для данной Modbus-строки без последних 2 байт.
        ModbusBytes = bytes.fromhex(sys.argv[2])
        crcExisted = ModbusBytes[-2:]
        ModbusBytes = ModbusBytes[:len(ModbusBytes) - 2]
        crcNEW = crc16.crc16(ModbusBytes)
        if (crcExisted == crcNEW):
            # sldkjflsjdflsdjflsjdf
            print("CRC is correct.")
            if (sys.argv[1] != '-p'):
                # Дешифровка Modbus-сообщения как Pool.
                print("Дешифровка Modbus-сообщения как Pool.")
            elif (sys.argv[1] != '-r'):
                # Дешифровка Modbus-сообщения как Request.
                print("Дешифровка Modbus-сообщения как Request.")
        else:
            print("CRC isn't correct")
else:
    # Случай, когда нет аргументов в командной строке.
    # Выводим страницу помощи.
    HelpPage.printHelpPage()
