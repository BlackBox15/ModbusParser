##-------------------------------------------------
## Вывод help-страницы.
##-------------------------------------------------

### Проверка использования файла автономно или через import.
##if __name__ == "__main__":
    
def printHelpPage():
    print('''
    This is my simple Modbus parser.
    
    -h                      this help page
    -p "01 02 03 3d ff"     parsing a pool-string
    -r "01 02 03 3d ff"     parsing a request-string
    ''')
