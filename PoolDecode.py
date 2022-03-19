##-------------------------------------------------
## Дешифровка PDU (protocol data unit) как ответ.
## PDU - это Modbus-строка без CRC-суммы.
##-------------------------------------------------
def decode(inPDU):
    """
    Дешифровка Modbus-ответа от полевого устройства.

    inPDU - <bytes>, Modbus-сообщение без последних 2-х байт (без CRC).

    Результат выводится на экран в таблице.
    """
    
    # Количество байт с данными.
    bytesQuantity = inPDU[2]
    
    cntr = 0
    
    # Рисуем таблицу.
    print("-" * 30)
    print("Byte\tDescription")
    print("-" * 30)

    # Вывод на экран.
    print('''{0:#04x} \tDevice address
{1:#04x} \tFunctional code
{2:#04x} \tBytes quanity
        '''.format(*inPDU))
    
    # Рисуем таблицу.
    print("-" * 30)
    print("Data in bytes")
    print("-" * 30)
    
    for n in inPDU[3:bytesQuantity + 3]:
        print("{:#04x}".format(n))
