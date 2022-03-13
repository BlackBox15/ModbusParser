"""
Функция вычисления CRC-суммы.
"""
## В функцию передаём Модбас-строку
## внутри - разбираем её на сегмент данных и CRC-суммы (крайние 2 байта)
## пересчитываем CRC-сумму для сегмента данных и сравниваем с существующим
## значением CRC-суммы.

##-------------------------------------------------
## Вычисление CRC-16 контрольной суммы.
##-------------------------------------------------


def crc16(dataModbus):
    """
    Вычислиение CRC16.

    dataModbus - <bytes>, передаём Modbus-сообщение.
    CRCreg - <int>, возвращаемое значение
    """
    # Полином для вычисления CRC.
    CRCPolynome_inv = 0xA001
    # Вычисленная CRC-сумма.
    CRCreg = 0xFFFF
##    # Байт-массив из Modbus-строки, неизменяемый (immutable).
##    dataModbus = bytes.fromhex(inputString)

    # Проходим через весь массив байт за исключением последних 2-х байт.
    for i in range(len(dataModbus)):
        # For is here.
        #
##        print("{0:#x}".format(dataModbus[i]))   # Actual type output string representing.

        # XOR'им i-й байт с контрольной суммой.
        CRCreg ^= dataModbus[i]
        
        # Побитовые операции.
        for j in range(8):
            
            if (CRCreg & 1) == 1:
                CRCreg >>= 1
                CRCreg ^= CRCPolynome_inv
            else:
                CRCreg >>= 1
            
    return CRCreg
            
##    print("{0:#x}".format(CRCreg))

