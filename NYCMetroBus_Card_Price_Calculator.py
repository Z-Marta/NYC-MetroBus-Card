'''program helping calculating the amount on a MetroBus card and the price of the trip.'''

'''ask if they have a card, if not if they want it.
ask the age: different price for different ages;
ask where they want to go: choose 1 of the listed station
said the amount of the ticket
check if they have enough money and if not, ask if they want to add extra money;

'''

'''
65 + = $1.45
MetroCard = $1
Base Fare = $2.90 ($5.80 minimum)
Express Bus fare = $7.00
7-Day Unlimited = $34
7-Day Express Bus Plus = $64.00
30-Day Unlimited fare = $132
Single Ride ticket = $3.25'''

import random

def get_card_number_end ():
    return str(random.randint(1, 999)).zfill(3)

print('Welcome to the Vending Machine in the Canal Street Station.')
print('Do you have a MetroBus Card? y/n')
metro_card = input()
if metro_card == 'y':
    print('please insert your card.')
    print('Reading...')
    card_number = get_card_number_end
    print(f'This are the information about the MetroCard # *****{card_number}:')
    money_inside = round(random.uniform(0,50), 2)
    print(f'Money Available: {money_inside} $')
    '''print('Do you want to add Money for a Single Ride base or purchase a Day Unlimited/Express Bus Plan?')
    choise = input()
    if choise == 'Money':
        print()'''
else:
    no_card = input ('Would you like to by a new one for the price of 1$? y/n' )
    if no_card == 'y':
        print('Confirming transaction...')
        print('Transaction confirmed. Thank you for purching a New MYC MetroBub Card.')
        card_number = get_card_number_end
        money_inside = 0
        print(f'This are the information about the MetroCard # *****{card_number}:')
        print(f'Money Available: {money_inside} $')
    else:
        print('Is it possible to buy just a Single Ride Fair. A Single Ride Card is not refillable and you can use once. Ask to the drive to a Paper Transfer on the first bus you bord if you want to transfer betweens buses.')
        no_Single_rise = input ('Do you want procede to buy a Single Ride Ticket? y/n' )
    