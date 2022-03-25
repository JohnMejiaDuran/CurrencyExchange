var1 = {
    "COP":1,
    "USD":2,
    "ARS":3,
    "CLP":4
}

var2 = {
    "USD":1,
    "COP":2,
    "ARS":3,
    "CLP":4
}

def converter(money,money2,dolar,dolar2):

    
    if option1 ==1 and option2==1 or option1==3 and option2 ==1 or option1==4 and option2==1:
        coin = float(input(f'How many {money} have you?: '))
        result=coin/dolar
        result=str(round(result,2))
        print(f'You have {result} {money2}')
    elif option1==1 and option2==3 or option1==1 and option2==4 or option1==3 and option2==1 or option1==3 and option2==4 or option1==4 and option1==1 or option2==4 and option2==3 or option1==3 and option2==2:
        coin= float(input(f'How many {money} you have?'))
        result=coin/dolar*dolar2
        result=str(round(result,2))
        print(f'You have {result} {money2}')
    else:
        coin = float(input(f'How many Dollars have you?: '))
        result=coin*dolar
        result=str(round(result,2))
        print(f'you have {result} {money}')
    
    

   


option1 =int(input(f'{var1} choose an option: '))
option2 =int(input(f'{var2} choose an option: '))
if option1 ==1 and option2 ==1 or option1==2 and option2==2:
    converter('Colombian Peso','Dollars',3815)
elif option1 ==3 and option2 ==1 :
    converter('Argentine Peso','Dollars', 110.17)
elif option1 ==4 and option2 ==1 or option1==2 and option2==4: 
    converter('Chilean Peso','Dollars', 796.88)
elif option1==1 and option2==3 or option1==3 and option2==2:
    converter('Colombian peso','Argentine Peso',3815,110.17)
elif option1==1 and option2==4 or option1==4 and option2==2:
    converter('Colombian Peso','Chilean Peso',3815,796.88)

else:
    print('Write a correct answer')

if '__name__'=='__main__':
    converter()
    