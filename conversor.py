menu = """ 
Welcome to this Money Converter

Choose one option

1. USD to COP
2. COP to USD
3. USD to MXN
4. MXN to USD
5. CLP to USD
6. USD to CLP

"""

def converter(money,dolar):

    coin = float(input(f'How many money have you?: '))
    if option % 2 !=0:
        result=coin*dolar
        result=str(round(result,2))
        print (f'You have {result} {money}')
    else:
        result=coin/dolar
        result=str(round(result,2))
        print (f'You have {result} Dollars')

option =int(input(menu))
if option ==1:
    converter('Colombian pesos',3815)
elif option ==2:
    converter('Colombian pesos',3815)
elif option ==3:
    converter('Mexican pesos', 20.37)
elif option ==4:
    converter('Mexican pesos', 20.37)
elif option ==5:
    converter('ARS', 20.37)
elif option ==6:
    converter('ARS', 20.37)
else:
    print('Write a correct answer')

if '__name__'=='__main__':
    converter()
    