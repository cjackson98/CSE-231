#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:42:07 2017

@author: chrisjackson
"""
    ###########################################################
    #  CSE 231 Project 2
    #
    #  Ask for price
    #    make sure price is positive
    #    ask for dollars paid
    #    make sure dollars paid is more than the price
    #       count change of the difference of price and dollars
    #       output change
    #       if requires more change than in mahcine, move to next lvl coin
    #       if out of coins output no more coins
    ###########################################################
q=10
d=10
n=10
p=10
quarters=0
dimes=0
nickels=0
pennies=0
print('Welcome to change-making program.')
print('Stock:',int(q),'quarters,',int(d),'dimes,',int(n),'nickels, and',\
      int(p),'pennies')
while(q>0 or d>0 or n>0 or p>0):#while coins are still in the machine
    a=input("Enter the purchase price (xx.xx) or 'q' to quit: ")
    if(a=='q'):
        break
    else:
        price=float(a)#convert price to a float and *100 to remove decimal
        price=round(price*100)
    if price<0:
        print('Error: purchase price must be non-negative.')#NEXT FEW BLOCKS\
        #MAKE SURE THE PRICE IS + AND THE DOLLARS PAID IS > THAN THE PRICE
        print('Stock:',int(q),'quarters,',int(d),'dimes,',\
              int(n),'nickels, and',int(p),'pennies')
        continue
    else:
        b=input('Input dollars paid (int): ')
        paid=float(b)
        paid=round(paid*100)
        while price>paid:
            print('Error: insufficient payment.')
            b=input('Input dollars paid (int): ')
            paid=float(b)
            paid=round(paid*100)
        if paid>=price:#count change
            paid=float(b)
            paid=round(paid*100)
            diff=paid-price
            if price==paid:
                print('No change.')
                print('Stock:',int(q),'quarters,',int(d),'dimes,',\
                      int(n),'nickels, and',int(p),'pennies')
                continue
            if(diff>((q*25)+(d*10)+(n*5)+(p*1))):#double check if theres enough coins
                q=0
                d=0
                n=0
                p=0
                print('Error: ran out of coins.')
                break
            while diff>=25:
                if(q==0):
                    break
                quarters=diff//25
                diff=diff-(quarters*25)
                if(quarters>=q):#if out of quarters, move to dimes
                    quarters=quarters-q
                    diff+=(quarters*25)
                    quarters=q
                    q=0
                else:
                    q=q-quarters
                    break
            while diff>=10:
                if(d==0):
                    break
                dimes=diff//10
                diff=diff-(dimes*10)
                if(dimes>=d):#if out of dimes move to nickels etc
                    dimes=dimes-d
                    diff+=(dimes*10)
                    dimes=d
                    d=0
                    #print('Dimes:', int(dimes))
                else:
                    d=d-dimes
                    #print('Dimes:', int(dimes))
                    break
            while diff>=5:
                if(n==0):
                    break
                nickels=diff//5
                diff=diff-(nickels*5)
                if(nickels>=n):
                    nickels=nickels-n
                    diff+=(nickels*5)
                    nickels=n
                    n=0
                else:
                    n=n-nickels
                    break
            while diff>=1:
                if(p==0):
                    print('Error: ran out of coins.')
                    break
                pennies=diff//1
                diff=diff-(pennies*1)
                if(pennies>=p):
                    print('Error: ran out of coins.')
                else:
                    p=p-pennies
    #OUTPUT FINAL CHANGE
    print('Collect change below: ')
    if(quarters!=0):
        print('Quarters:', int(quarters))
        quarters=0
    if(dimes!=0):
        print('Dimes:', int(dimes))
        dimes=0
    if(nickels!=0):
        print('Nickels:', int(nickels))
        nickels=0
    if(pennies!=0):
        print('Pennies:', int(pennies))
        pennies=0
    print('Stock:',int(q),'quarters,',int(d),'dimes,',int(n),'nickels, and'\
          ,int(p),'pennies')