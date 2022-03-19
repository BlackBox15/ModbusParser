##-------------------------------------------------
## Дешифровка PDU (protocol data unit) как запрос.
## PDU - это Modbus-строка без CRC-суммы.
##-------------------------------------------------

## Принимает 


def decode(inPDU):
##    print('Decode argument as Request.')
##    for i in inPDU:
##        print("{0:#x}".format(i))
    
    # Рисуем таблицу.
    print("-" * 30)
    print("Byte\tDescription")
    print("-" * 30)
    
##    print("{0:#x}\t\t1\tDevice address".format(inPDU[0]))
##    print("{0:#x}\t\t2\tFunctional code".format(inPDU[1]))
##    print("{0:#x} {1:#x}\t3,4\t1st register address".format(inPDU[2], inPDU[3]))
##    print("{0:#x} {1:#x}\t5,6\tNums of register to read".format(inPDU[4], inPDU[5]))

    if (len(inPDU) == 6):
        print('''
{0:#04x} \t Device address
{1:#04x} \t Functional code
{2:#04x}{3:02x} \t 1st register address
{4:#04x}{5:02x} \t Nums of register to read
            '''.format(*inPDU))

