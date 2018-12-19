# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:27:25 2017

@author: jack1391
"""

import math
def openfile():
    while 1==1:
        try:
            filename=input('Enter a file name: ')
            file=open(filename,'r')
            break
        except FileNotFoundError:
            print('Unable to open file. Try again')
    return file
    file=open(filename,'r')
    return file

def main():
    count=[0,0,0,0,0,0,0,0,0]
    holder=[]
    file=openfile()
    ctr=1
    ctr2=0
    for line in file:
        line=line.strip()
        if line[0] is not '0':
            ctr2+=1
#        while ctr==1:
        if line[0]=='0':
            continue
        if line[0]=='1':
            count[0]+=1
            #ctr+=1
            continue
        if line[0]=='2':
            count[1]+=1
            #ctr+=1
            continue
        if line[0]=='3':
            count[2]+=1
            #ctr+=1
            continue
        if line[0]=='4':
            count[3]+=1
            #ctr+=1
            continue
        if line[0]=='5':
            count[4]+=1
            #ctr+=1
            continue
        if line[0]=='6':
            count[5]+=1
            #ctr+=1
            continue
        if line[0]=='7':
            count[6]+=1
            #ctr+=1
            continue
        if line[0]=='8':
            count[7]+=1
            #ctr+=1
            continue
        if line[0]=='9':
            count[8]+=1
            #ctr+=1
            continue
    print('{} {} {}'.format('Digit','Percent','Benford'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('1:',round(float(count[0]/ctr2)*100,1),'(30.1%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('2:',round(float(count[1]/ctr2)*100,1),'(17.6%)'))
    print(' {:4^s} {:^4.1f}% {:4^s}'.format('3:',round(float(count[2]/ctr2)*100,1),'(12.5%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('4:',round(float(count[3]/ctr2)*100,1),'( 9.7%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('5:',round(float(count[4]/ctr2)*100,1),'( 7.9%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('6:',round(float(count[5]/ctr2)*100,1),'( 6.7%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('7:',round(float(count[6]/ctr2)*100,1),'( 5.8%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('8:',round(float(count[7]/ctr2)*100,1),'( 5.1%)'))
    print(' {:4>s} {:>4.1f}% {:4>s}'.format('9:',round(float(count[8]/ctr2)*100,1),'( 4.6%)'))
    
    
main()