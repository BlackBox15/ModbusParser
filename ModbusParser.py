"""
Дешифровка Modbus-сообщения.

-r "string of hex" - дешифровка Modbus-сообщения, как request
-p "string of hex" - дешифровка Modbus-сообщения, как pool

Результат выводится на экран в таблице.
"""

# импорт для возможности чтения входящих аргументов
import sys
import crc16
import HelpPage
import RequestDecode
import PoolDecode
##-------------------------------------------------
## Тестовая строка
## -r "01 03 d7 f3 32 ff 78 1a"             CRC isn't correct
## -r "01 03 d7 f3 32 ff d9 6d"             CRC is correct
##
## -p "01 03 06 03 fd 45 e1 2f 5a 95 a3"    CRC is correct
## -r "01 03 3f 00 00 0c 49 db"             CRC is correct
##-------------------------------------------------
##print("\n", "." * 10, "MODBUS parser", "." * 10, "\n")

if (len(sys.argv) > 1):
    # Есть аргументы в CLI.
    if (sys.argv[1] != '-p') and (sys.argv[1] != '-r') :
        # Страница помощи при отсутствии ключей в CLI.
        HelpPage.printHelpPage()
    elif (sys.argv[2] != ''):
        # Есть ключ -r, или -p.
        # Есть наличие Modbus-строки в аргументе CLI.
        # Парсим 2-й аргумент из hex в bytes.
        ModbusBytes = bytes.fromhex(sys.argv[2])
        # Существующая CRC-сумма из Modbus-сообщения.
        # Расположена как 2 последних байта в сообщении.
        crcExisted = ModbusBytes[-2:]
        # Modbus-сообщение без последних 2-х байт - это PDU.
        # Protocol Data Unit.
        pdu = ModbusBytes[:len(ModbusBytes) - 2]
        # Актуальный CRC для полученного PDU.
        crcNew = (crc16.crc16(pdu)).to_bytes(2, 'little')

        if (crcExisted == crcNew):
            # Совпадение существующей и расчётной CRC.
            print("CRC is correct.")
            
            if (sys.argv[1] == '-p'):
                # Дешифровка Modbus-сообщения как Pool.
                print("Decoding as a Pool.")
                PoolDecode.decode(pdu)
            elif (sys.argv[1] == '-r'):
                # Дешифровка Modbus-сообщения как Request.
                print("Decoding as a Request.")
                RequestDecode.decode(pdu)
        else:
            print("CRC isn't correct")
            
else:
    # Нет аргументов в командной строке.
    # Выводим страницу помощи.
    HelpPage.printHelpPage()
