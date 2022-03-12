##-------------------------------------------------
## Дешифровка PDU (protocol data unit) как ответ.
## PDU - это Modbus-строка без CRC-суммы.
##-------------------------------------------------

def decode(inPDU):
    # Количество байт с данными.
    bytesQuantity = inPDU[2]
    cntr = 0
    
    print("-" * 30)
    print("Byte\tDescription")
    print("-" * 30)

    # Вывод на экран.
    print('''{0:#x} \tDevice address
{1:#x} \tFunctional code
{2:#x} \tBytes quanity
        '''.format(*inPDU))

    for n in inPDU[3:bytesQuantity + 3]:
        print("{:x}".format(n))
