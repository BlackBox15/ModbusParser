## Функция вычисления CRC-суммы

## В функцию передаём Модбас-строку
## внутри - разбираем её на сегмент данных и CRC-суммы (крайние 2 байта)
## пересчитываем CRC-сумму для сегмента данных и сравниваем с существующим
## значением CRC-суммы.

##-------------------------------------------------
## Вычисление CRC-16 контрольной суммы.
##-------------------------------------------------


def crc16(inputString):
##  Байт-массив из Modbus-строки, неизменяемый (immutable).
    bytesOfString = bytes.fromhex(inputString)

    for b in bytesOfString:
##        print(f"%0#x" % b)        # Old type output string representing.
        print("{0:#x}".format(b))   # Actual type output string representing.
    
## Существующее значение CRC хранится в последних 2-х байтах
## Modbus-сообщения.
    existCRC16 = bytesOfString[(len(bytesOfString) - 1)] + \
                 bytesOfString[(len(bytesOfString) - 2)]

crc16("01 03 43 8f b3 78")  # Just for testing.
