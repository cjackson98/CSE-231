# -*- coding: utf-8 -*-
"""
CSE 231 Project 3
Ask for input
    check for vowels
        if found, add vowel to list and stop checking for that vowel
    check for consonants
    remove duplicate consonants
    end loop if all vowels found or 5 consonants
    format and print
"""
#initialize variables that remain through each input
vowels=""
cons_first=""
cons_len=0
vowels_len=0
a=False
e=False
i=False
o=False
u=False
while 1==1:
    word=input('Input a word: ')#get input
    word=word.lower()
    y=0
    holder=""
    VOWELS="aeiou"#initialize variables
    CONS="bcdfghjklmnpqrstvwxyz"
    for x in word:#check each position in word for variables
        if word[y] in VOWELS:
            """
            if one variable is found it is set to true and if all variables
            are true it will break out of the while statement below. also
            adds vowels to a list
            """
            if word[y]=="a" and a==False:
                a=True
                vowels=vowels+word[y]
            elif word[y]=="e" and e==False:
                e=True
                vowels=vowels+word[y]
            elif word[y]=="i" and i==False:
                i=True
                vowels=vowels+word[y]
            elif word[y]=="o" and o==False:
                o=True
                vowels=vowels+word[y]
            elif word[y]=="u" and u==False:
                u=True
                vowels=vowels+word[y]
        y+=1
    while word[-1] not in VOWELS:
        """
        find consonants after vowel by checking last letter and if it is not a
        vowel, moving it. Once it finds the last vowel in the original word
        you will have a list of consonants after the vowel in reverse order
        """
        holder=holder+word[-1]
        word=word[-1]+word
        word=word[0:-1]
    holder=holder[::-1]#reverse the list of consonants
    cons_first=cons_first+holder  
    if a and e and i and o and u:#if all vowels found, break while loop
        break
    if len(cons_first)>=5:#if 5 consonants found, break while loop
        break
cons_final=cons_first.\
join(sorted(set(cons_first), key=cons_first.index))#remove duplicate consonants
#double check that the code above didnt add extra consonants
if len(cons_final)>len(cons_first):
    cons_final=cons_first
vowels_len=len(vowels)#get length of vowels and consonants below
cons_len=len(cons_final)
#format and print
print("\n"+"="*12)
print("{:8s}{:7s} | {:12s}{:7s}".\
      format("vowels","length","consonants","length"))
print("{:8s}{:<7d} | {:12s}{:<7d}".\
      format(vowels,vowels_len,cons_final,cons_len))