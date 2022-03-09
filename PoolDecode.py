##-------------------------------------------------
## Дешифровка PDU (protocol data unit) как ответ.
## PDU - это Modbus-строка без CRC-суммы.
##-------------------------------------------------

def decode(inPDU):
    bytesQuantity = 
    print('''
{0:#x} \t 1 \t Device address
{1:#x} \t 2 \t Functional code
{2:#x} \t 3 \t Bytes quanity

{2:#x}{3:x} \t 3,4 \t 1st register address
{4:#x}{5:x} \t 5,6 \t Nums of register to read
        '''.format(*inPDU))
