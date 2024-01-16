'''Vending machine Metro Card program helping buy MetroBus card and tickets.'''

import random
import time

TICKET_LIST = {1:'Base Fare = $2.90', 2:'Express Bus Fare = $7.00', 3: '7-Day Unlimeted = $34', 4: '7-Day Express Bus Plus = $64', 5: '30-Day Unlimited Fare = $132'}
TICKET_PRICE = {1 : 2.90, 2 : 7.00, 3 : 34.00, 4 : 64.00, 5 : 132.00}

def im_working():
    time.sleep(1)
    print()

def no_mistake():
    print("You must type y for Yes or n for No. ")

def no_mistake_1():
    print("You must type Continue or Exit. ")

def no_mistake_2():
    print("You must type a number between 1 and 5. ")

# This function creates random 3 number of 8 digit number card. The other 5 are hidden by * for privacy issue.
def get_card_number_end ():
    return str(random.randint(1, 999)).zfill(3)

# This function asks the user to insert a valide amount of money.
def add_money():    
    while True:
        try:
            insert_money = float(input("Please, insert money. "))
        except ValueError:
            im_working()
            print("Sorry, we cannot process this request.")
            im_working()
            print("Please, try again.")            
            continue
        if insert_money < 0:
            im_working()
            print("Sorry, we cannot process this request.")
            im_working()
            print("Please, try again.")
        else:
            break
    return insert_money

# This function shows to the user how many money needs to insert to by the choosed ticket. 
# It shows the differents between the money in the Metro Card and the price of the ticket.
def ask_money(money, price):
    need_money = round ((money - price), 2)
    im_working()
    print('You don\'t have enough money to purchase the ticket.')
    im_working()
    print('Please insert the correct amount')
    im_working()
    print(f'You need extra {abs(need_money)}$ to buy the ticket.')
    money_inserted = add_money()
    money += money_inserted
    return money

# This function calculates if the user insert enough money to update the balance in the Metro card and buy the choosed ticket.
def enough_money (money, price):
    while money < price:
        money = ask_money(money, price)
    im_working()    
    print('You have enough money to purchase the ticket.')
    return money - price

# This function shows to the user how many money needs to insert to by the choosed ticket. 
def ticket_option():
    im_working()
    print('Please, choose one of the following option:')
    im_working()
    print(TICKET_LIST)
    im_working()
    print('You get a free trasfer from the subway to a bus, bus to subway, or bus to bus.')
    im_working()
    print('If you transfer from  the subway or local bus to an express bus,')
    print('you\'ll be charged the difference between the subway or bus fare and the express bus fare unless you have a 7-Day Unlimited Express Bus Plus MetroCard.')
    im_working()
    
    while True:
        try:
            ticket_chosen = int(input('Wich ticket would you like to by? use only the number: '))
            ticket = TICKET_LIST[ticket_chosen]

        except KeyError:
            im_working()
            no_mistake_2()
            im_working() 
            continue

        except ValueError:
            im_working()
            no_mistake_2()
            im_working()        
            continue
        
        else:
            break
    
    im_working()
    print(f'You choosed the option: {ticket}')
    im_working()
    right_ticket = input(f'Do you want to buy the {ticket} ticket? y/n ').lower()
    return ticket, ticket_chosen, right_ticket

# This function returns the money inside the metrobus card and the ticket bought. It calls the functions 'ask_money' and 'enough_money'   
def buy_ticket(money_inside):
    im_working()
    buy_ticket = input('Would you like to buy a ticket? y/n ').lower()
    while buy_ticket != 'y' and buy_ticket != 'n':
        no_mistake()
        buy_ticket = input().lower()
    if buy_ticket == 'y':
        ticket, ticket_chosen, right_ticket = ticket_option()
        
        while right_ticket == 'n':
            ticket, ticket_chosen, right_ticket = ticket_option()
        
        price = TICKET_PRICE[ticket_chosen]
        if ticket_chosen == 1:
            price = 5.80
            im_working()
            print('To buy this ticket, you need to have minimum $5.80 .')
                
            while money_inside < price:
                money_inside = ask_money(money_inside, price)
            money_inside -= price
        else:
            money_inside = enough_money(money_inside, price)
        im_working()
        print('Payment is processing...')
        im_working()
        print('Your payment have been confermed, thank you.')

        return money_inside, ticket
    else:
        im_working()
        print('You didn\'t buy any new ticket in this transaction.')
        return money_inside, 'No Ticket'
        
# This function initialize the metrobus card at the biggining of the program, randomly choose the end of the number and the money inside the card. 
def init_metrocard ():
    im_working()
    print('Please insert your card.')
    im_working()
    print('Reading...')
    card_number = get_card_number_end()
    money_inside = round(random.uniform(0,50), 2)
    ticket_inside = 'No ticket'
    return card_number, money_inside, ticket_inside

# This function shows to the user the attribute of their card: money, ticket and card number.    
def start(card_number, money_inside, ticket_inside):
    im_working()
    print(f'This are the information about the MetroCard # *****{card_number}:')
    im_working()
    print(f'Money Available: {round(money_inside, 2)} $')
    im_working()
    print(f'Ticket Available to use: {ticket_inside}')

#begginning of the program  

im_working()     
print('Welcome to the Vending Machine in the Canal Street Station.')
im_working()
print('Do you have a MetroBus Card? y/n')
metro_card = input().lower()
while metro_card != 'y' and metro_card != 'n':
    no_mistake()
    metro_card = input().lower()
if metro_card == 'y':
    card_number, money_inside, ticket_inside = init_metrocard()
    start(card_number, money_inside, ticket_inside)
    money_inside, ticket_inside = buy_ticket(money_inside)
else:
    im_working()
    no_card = input ('Would you like to by a new one for the price of 1$? y/n' ).lower()
    while no_card != 'y' and no_card != 'n':
        no_mistake()
        no_card = input().lower()
    if no_card == 'y':
        im_working()
        print('Confirming transaction...')
        im_working()
        print('Transaction confirmed. Thank you for purching a New MYC MetroBub Card.')
        card_number, money_inside, ticket_inside = init_metrocard()
        im_working()
        print('New MYC MetroBub Card need to be a balance of at least 5.80$, the price for 2 Base Fare as Pay-As-You-Go.')
        price = 5.80                
        while money_inside < price:
            money_inside = ask_money(money_inside, price)
            money_inside -= price
        im_working()
        print(f'This are the information about the MetroCard # *****{card_number}:')
        im_working()
        print(f'Money Available: {money_inside} $')
        im_working()
        print(f'Ticket Available to use: {ticket_inside}')
        im_working()
        money_inside, ticket_inside = buy_ticket(money_inside)   
    else:
        im_working()
        print('Is it possible to buy just a Single Ride Fair. A Single Ride Card is not refillable and you can use once.') 
        print('Ask to the drive to a Paper Transfer on the first bus you bord if you want to transfer betweens buses.')
        im_working()
        no_Single_rise = input ('Do you want procede to buy a Single Ride Ticket? y/n ' ).lower()
        price = 3.25
        while no_Single_rise != 'y' and no_Single_rise != 'n':
            no_mistake()
            no_Single_rise = input().lower()
        if no_Single_rise == 'y':
            im_working()
            print('The ticket cost 3.25$ . Please, insert the money')
            money = add_money()
            enough_money(money, price)
            im_working()
            print('you bought a single Ride Ticket. Please, don\'t forget to collect the item in the slot bihind.')
            im_working()
            print('Thank you to choose us.')
        else:
            print('Your selection is not valid. Please, select a valide option.')
            im_working()
        card_number = 'No MetroCard purchaced'
        money_inside = 0
        ticket_inside = 'Single Ride Fair'
        im_working()
next = input('What would you like to do? Continue or Exit ').lower()
while next != 'continue' and next != 'exit':
    no_mistake_1()
    next = input().lower()
if next == 'continue':
    start(card_number, money_inside, ticket_inside)
    im_working()
print('Thank you to use our Vending Machine. See you in the next trip! Have a Safe Journey.')