
print('Welcome to the Vending Machine in the Canal Street Station.')
print('Do you have a MetroBus Card?')
metro_card = input()
if metro_card == 'yes':
    print('please insert your card.')
    print('Reading...')
    print(f'This are the information about the MetroCard # *****567:')
    
    print('Do you want to add Money for a Single Ride base or purchase a Day Unlimited/Express Bus Plan?')
    choise = input()
    if choise == 'Money':
        print()