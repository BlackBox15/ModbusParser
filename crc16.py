## Функция вычисления CRC-суммы

## В функцию передаём Модбас-строку
## внутри - разбираем её на сегмент данных и CRC-суммы (крайние 2 байта)
## пересчитываем CRC-сумму для сегмента данных и сравниваем с существующим
## значением CRC-суммы.

##-------------------------------------------------
## Вычисление CRC-16 контрольной суммы.
##-------------------------------------------------


def crc16(inputString):
    
    # Полином для вычисления CRC.
    CRCPolynome_inv = 0xA001
    # Вычисленная CRC-сумма.
    CRCreg = 0xFFFF
    # Байт-массив из Modbus-строки, неизменяемый (immutable).
    dataModbus = bytes.fromhex(inputString)

    # Проходим через весь массив байт за исключением последних 2-х байт.
    for i in range(len(dataModbus) - 2):
        # For is here.
        #
        print("{0:#x}".format(dataModbus[i]))   # Actual type output string representing.

        # XOR'им байт с контрольной суммой.
        CRCreg ^= dataModbus[i]
        
        # Побитовые операции.
        for j in range(8):
            # For is here
            #
            CRCreg >>= 1
            
##            if (CRCreg & 1) == 1:
##                CRCreg >>= 1
##                CRCreg ^= CRCPolynome_inv
##            else:
##                CRCreg >>= 1
            

            
    print("0:#x".format(CRCreg))








##    for b in bytesOfString:
####        print(f"%0#x" % b)        # Old type output string representing.
##        print("{0:#x}".format(b))   # Actual type output string representing.
##    
#### Существующее значение CRC хранится в последних 2-х байтах
#### Modbus-сообщения.
##    existCRC16 = bytesOfString[(len(bytesOfString) - 1)] + \
##                 bytesOfString[(len(bytesOfString) - 2)]
##
crc16("01 03 43 8f b3 78")  # Just for testing.
