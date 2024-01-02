Invest = 500
Mike = int(input('Капитал Майкла:'))
Ivan = int(input('Капитал Ивана:'))

if Mike>500 and Ivan>500:
    print(2)
elif Mike>500 and Ivan<500:
    print('Mike')
elif Mike<500 and Ivan>500:
    print('Ivan')
elif (Mike + Ivan)>500:
    print(-1)
elif (Mike + Ivan)<500:
    print(0)
