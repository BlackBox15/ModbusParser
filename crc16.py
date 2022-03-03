## Функция вычисления CRC-суммы

## В функцию передаём Модбас-строку
## внутри - разбираем её на сегмент данных и CRC-суммы (крайние 2 байта)
## пересчитываем CRC-сумму для сегмента данных и сравниваем с существующим
## значением CRC-суммы.

lengthOfString = 0      # длина входной строки

def crc16(inputString):
##  Байт-массив из Modbus-строки.
    bytesOfString = bytearray.fromhex(inputString)

##    for b in bytesOfString:
##        print(b)
    
##  Существующее значение CRC.
    existCRC16 = bytesOfString[(len(bytesOfString) - 1)] + \
                 bytesOfString[(len(bytesOfString) - 2)]
