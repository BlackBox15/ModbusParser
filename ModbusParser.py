# импорт для возможности чтения входящих аргументов
import sys
import crc16
import HelpPage
import RequestDecode
##-------------------------------------------------
## Тестовая строка
## -r "01 03 d7 f3 32 ff 78 1a"    CRC isn't correct
## -r "01 03 d7 f3 32 ff d9 6d"    CRC is correct
##-------------------------------------------------
##print("\n", "." * 10, "MODBUS parser", "." * 10, "\n")

if (len(sys.argv) > 1):
    # Случай, когда есть аргументы в командной строке.
    if (sys.argv[1] != '-p') and (sys.argv[1] != '-r') :
        # Выводим страницу помощи.
        HelpPage.printHelpPage()
    elif (sys.argv[2] != ''):
        # У нас команда или -r, или -p.
        # Наличие Modbus-строки в аргументе командной строки.
        ModbusBytes = bytes.fromhex(sys.argv[2])
        # Вычисляем CRC для данной Modbus-строки без последних 2 байт.
        # Крайние 2 байта "срезаем" в отдельную переменную.
        crcExisted = ModbusBytes[-2:]
        # Modbus-сообщение без последних 2-х байт - это PDU.
        # Protocol Data Unit.
        pdu = ModbusBytes[:len(ModbusBytes) - 2]
        # Вычисляем CRC для полученного PDU.
        # Для сравнения.
        crcNew = (crc16.crc16(pdu)).to_bytes(2, 'little')
        
        if (crcExisted == crcNew):
            print("CRC is correct.")
            
            if (sys.argv[1] == '-p'):
                # Дешифровка Modbus-сообщения как Pool.
                print("Decoding as a Pool.")
            elif (sys.argv[1] == '-r'):
                # Дешифровка Modbus-сообщения как Request.
                print("Decoding as a Request.")
                RequestDecode.decode(pdu)
        else:
            print("CRC isn't correct")
            
else:
    # Случай, когда нет аргументов в командной строке.
    # Выводим страницу помощи.
    HelpPage.printHelpPage()
