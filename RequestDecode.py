##-------------------------------------------------
## Дешифровка PDU (protocol data unit) как запрос.
## PDU - это Modbus-строка без CRC-суммы.
##-------------------------------------------------

## Принимает 


def decode(inPDU):
##    print('Decode argument as Request.')
##    for i in inPDU:
##        print("{0:#x}".format(i))
    
##    print("-" * 30)
##    print("#\t\tByte\tDescription")
##    print("-" * 30)
##    print("{0:#x}\t\t1\tDevice address".format(inPDU[0]))
##    print("{0:#x}\t\t2\tFunctional code".format(inPDU[1]))
##    print("{0:#x} {1:#x}\t3,4\t1st register address".format(inPDU[2], inPDU[3]))
##    print("{0:#x} {1:#x}\t5,6\tNums of register to read".format(inPDU[4], inPDU[5]))

    print('''
        {0:#x}          1   Device address
        {1:#x}          2   Functional code
        {2:#x}{3:x}     3,4 1st register address
        {4:#x}{5:x}     5,6 Nums of register to read
        '''.format(for i in inPDU: i))

