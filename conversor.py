


menu = """ 
Welcome to this Money Converter

Choose one option

1. USD to COP
2. COP to USD

"""

def converter(money,dolar):

    peso = float(input(f'How many {money} have you?: '))
    if money == 'Dollars':
        result=dolar*peso
        result=str(result)
        print (f'You have {result} Colombian Pesos')
    else:
        result=peso/dolar
        result=round(result,2)
        print (f'You have {result} Dollars')

option =int(input(menu))
if option ==1:
    converter('Dollars',3815)
elif option ==2:
    converter('Colombian Pesos',3815)
else:
    print (input(menu))

if '__name__'=='__main__':
    converter()













            





# def run():
    
#     def conversor():
#         out = (coin * dolarprice
#         return out

        
        
        

    

#     if '__name__' == '__main__':
#         run()

    
    

