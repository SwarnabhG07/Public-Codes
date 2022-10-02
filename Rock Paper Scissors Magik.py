from itertools import repeat
import random

#Starting
z= 0
print ('Press ENTER to start the Game')
A = input ()
while (z==0):
    print('====================================================================================================================')
    print ('ROCK , PAPER , SCISSORS')
    print()
    print ('"Hello! I M SG your Opponent in this game,')
    print ('Wishing you all the best Playing Against me :-) " ')
    print ()
    print ('Choose Diificuly level')
    print ('1 = EASY')
    print ('2 = NORMAL')
    print ('3 = HARD')
    o = 0
    while (o==0):          
        print()
        n = int (input('Enter difficulty Level => '))
        print ()
        if ((n==1)or (n == 2) or (n==3)):
                   o = o +1
        else:
             print ('Invalid input, pls enter 1 , 2 or 3')
    if (n==1):
        print ('Difficulty => EASY')
        print()
        a= 0
        while (a==0):
            p =0 
            while (p==0):
                i = int (input('ENTER the number of Rounds you want to Play => '))
                if (i==0):
                    print ('Are You Scared to Play with me??')
                elif (i>0):
                    p = p +1
                else:
                    print ('Invalid input, pls enter 1 , 2 or 3')
                    print ()
            print ('press "ENTER" to START the turn of the game ')
            b= input()
            h = 0
            j = 0
            for k in range (1,i+1):
                print ()
                print('ENTER =>')
                print ('1 = ROCK')
                print ("2 = PAPER")
                print ('3 = SCISSORS')
                d = 0 
                while (d==0):
                    print ()
                    c = int (input('Enter Your Chance => '))
                    print ()
                    if ((c==1)or (c == 2) or (c==3)):
                        if (c==1):                           
                            print ('You Used => Rock')
                            d= d +1
                        elif (c==2):                           
                            print ('You Used => Paper')
                            d = d +1
                        elif ( c == 3):                            
                            print ('You Used => scissors')
                            d = d +1
                    else:
                            print ('Invalid input, pls enter 1 , 2 or 3')
                            print ()
                            repeat
                if (c==1):
                    e = random.randint (4,5)
                    if (e==4):
                        print ('SG Used => Scissors' )
                        print ()
                        print ('YOU won this Round!!')
                        h = h +1
                    if (e==5):
                        print ('SG Used => Rock')
                        print ()
                        print ('Draw')
                if (c==2):
                    e = random.randint (1,2)
                    if (e==1):
                        print ('SG Used => Rock' )
                    if (e==2):
                        print ('SG Used => Paper')
                if (c==3):
                    e = random.randint (2,3)
                    if (e==2):  
                        print ('SG Used => Paper' )
                    if (e==3):  
                        print ('SG Used => Scissors')
                print ()
                #counter
                if ((c==1) and (e==1)):
                    print ('Draw')
                if ((c==1) and (e==2)):
                    j = j+1
                    print ('SG won this Round!!')
                if ((c==1) and (e==3)):
                    h = h +1
                    print ('YOU won this Round!!')       
                if ((c==2) and (e==1)):
                    h = h +1
                    print ('YOU won this Round!!')
                if ((c==2) and (e==2)):
                    print ('Draw')
                if ((c==2) and (e==3)):
                    j = j +1
                    print ('SG won this Round!!')
                if ((c==3) and (e==1)):
                    j = j +1
                    print ('SG won this Round!!')
                if ((c==3) and (e==2)):
                    h = h +1
                    print ('YOU won this Round!!')
                if ((c==3) and (e==3)): 
                    print ('Draw')
                print ()
                print ('SCORE => ',end="")
                print ('You = ',h,end='')
                print (' V/S SG = ',j)
                print('-----------------------------------------------------------')
                #winning block
                l = i/2
                if (h>l):
                    print()
                    print ('Final Score => You = ',h, end = '' )
                    print (' V/S SG = ' , end= '' )
                    print (j)
                    print ('Final Result => YOU WON!!')
                    break 
                if (j>l):
                    print()
                    print ('Final Score => You = ',h, end = '' )
                    print (' V/S SG = ' , end= '' )
                    print (j)
                    print ('Final Result => YOU LOST...')
                    break                    
            if (h<l):
                    if (h>j):
                        print()
                        print ('Final Score => You = ',h, end = '' )
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => YOU WON!!')                        
            if (j<l):
                    if (j>h):
                        print()
                        print ('Final Score => You = ',h, end = '' )
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => YOU LOST..')                
            if (j==h):
                    print()
                    print ('Final Score => You = ',h, end = '' )
                    print (' V/S SG = ' , end= '' )
                    print (j)
                    print ('Final Result => DRAW!!')    
            print ()
            print ( 'Do you want to Quit??')
            print ()
            print('Enter 1 continue')
            print ('Enter 0 to quit')
            f =0
            while (f==0):
                print ()
                g = int(input ('Enter 1 or 0=> '))
                if ((g==1) or (g==0)):
                    f= f+1
                else:
                    print ('Invalid input, pls enter 0 or 1')
                    print()
                    f = f+ 0
            if (g==1):
                a = a +1
            if (g==0):
                a =a + 1
                z = z +1
    if (n==2):
        print ('Difficulty => NORMAL')
        print()
        a=0
        while (a==0):
            p =0 
            while (p==0):
                i = int (input('ENTER the number of Rounds you want to Play => '))
                if (i==0):
                    print ('Are You Scared to Play with me??')
                elif (i>0):
                    p = p +1
                else:
                    print ('Invalid input, pls enter 1 , 2 or 3')
                    print ()
            print ('press "ENTER" to START the turn of the game ')
            b= input()
            h = 0
            j =0
            for k in range (1,i+1):
                print ()
                print('ENTER =>')
                print ('1 = ROCK')
                print ("2 = PAPER")
                print ('3 = SCISSORS')
                d = 10 
                while (d==10):
                    print ()
                    c = int (input('Enter Your Chance => '))
                    print ()
                    if ((c==1)or (c == 2) or (c==3)):
                        if (c==1):
                            print ('You Used => Rock')
                            d =d +1
                        elif (c==2):
                            print ('You Used => Paper')
                            d = d +1
                        elif (c==3):
                            print ('You Used => Scissors')
                            d = d+1
                    else:
                            print ('Invalid input, pls enter 1 , 2 or 3')
                            print ()           
                            repeat
                e = random.randint(1,3)
                if (e==1):
                    print ('SG Used => Rock')
                if (e==2):
                    print ('SG Used => Paper')
                if (e==3):
                    print ('SG Used => Scissors')
                print ()
                #counter
                if ((c==1) and (e==1)):          
                    print ('Draw')
                if ((c==1) and (e==2)):
                        j = j+1
                        print ('SG won this Round!!')
                if ((c==1) and (e==3)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==2) and (e==1)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==2) and (e==2)):          
                        print ('Draw')
                if ((c==2) and (e==3)):
                        j = j +1
                        print ('SG won this Round!!')
                if ((c==3) and (e==1)):
                        j = j +1
                        print ('SG won this Round!!')
                if ((c==3) and (e==2)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==3) and (e==3)):          
                        print ('Draw')
                print ()
                print ('SCORE => ',end="")
                print ('You = ',h,end='')
                print (' V/S SG = ',j)
                print('-----------------------------------------------------------')        
                #winning bolck
                l = i/2
                if (h>l):
                    print()
                    print ('Final Score => You = ',h , end = '' )
                    print (' V/S SG = ' , end= '' )
                    print (j)
                    print ('Final Result => YOU WON!!')
                    break 
                if (j>l):
                        print()
                        print ('Final Score => You = ',h , end = '' )
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => YOU LOST...')
                        break
            if (h<l):
                        if (h>j):
                            print()
                            print ('Final Score => You = ',h , end='' )
                            print (' V/S SG = ' , end= '' )
                            print (j)
                            print ('Final Result => YOU WON!!')
            if (j<l):
                        if (j>h):
                            print()
                            print ('Final Score => You = ',h , end='' )
                            print (' V/S SG = ' , end= '' )
                            print (j)
                            print ('Final Result => YOU LOST..')
            if (j==h):
                        print()
                        print ('Final Score => You = ',h , end= '')
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => DRAW!!')    
            print ()
            print ( 'Do you want to Quit??')
            print ()
            print('Enter 1 continue')
            print ('Enter 0 to quit')
            f =0
            while (f==0):
                    print ()
                    g = int(input ('Enter 1 or 0=> '))
                    if ((g==1) or (g==0)):
                        f= f+1
                    else:
                        print ('Invalid input, pls enter 0 or 1')
                        print()                   
            if (g==1):
                    a = a +1
            if (g==0):
                    a =a + 1
                    z = z +1
    if (n==3):
        print ('Difficulty => HARD')
        a=0
        while (a==0):
            print ()
            p=0
            while (p==0):
                i = int (input('ENTER the number of Rounds you want to Play => '))
                if (i==0):
                    print ('Are You Scared to Play with me??')
                elif (i>0):
                    p = p +1
                else:
                    print ('Invalid input, pls enter 1 , 2 or 3')
                    print ()
            print ('press "ENTER" to START the turn of the game ')
            b= input()
            h = 0
            j =0
            for k in range (1,i+1):
                print ()
                print('ENTER =>')
                print ('1 = ROCK')
                print ("2 = PAPER")
                print ('3 = SCISSORS')
                d = 0 
                while (d==0):
                    print ()
                    c = int (input('Enter Your Chance => '))
                    print ()
                    if ((c==1)or (c == 2) or (c==3)):
                        if (c==1):
                            print ('You Used => Rock')
                            d = d +1
                        elif (c==2):
                            print ('You Used => Paper')
                            d = d+1
                        elif (c==3):
                            print ('You Used => Scissors')
                            d = d +1
                        else:
                            print ('Invalid input, pls enter 1 , 2 or 3')
                            print ()
                            repeat
                if (c==1):
                    e = random.randint (1,2)
                    if (e==1):
                        print ('SG Used => Rock' )
                    if (e==2):
                        print ('SG Used => Paper')
                if (c==2):
                    e = random.randint (2,3)
                    if (e==2):
                        print ('SG Used => Paper' )
                    if (e==3):
                        print ('SG Used => Scissors')
                if (c==3):
                    e = random.randint (4,5)
                    if (e==4):  
                        print ('SG Used => Scissors' )
                        print ()
                        print ('Draw')
                    if (e==5):  
                        print ('SG Used => Rock') 
                        print ()
                        print ('SG won this Round!!')
                        j = j +1
                print ()
                #counter
                if ((c==1) and (e==1)):          
                    print ('Draw')
                if ((c==1) and (e==2)):
                        j = j+1
                        print ('SG won this Round!!')
                if ((c==1) and (e==3)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==2) and (e==1)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==2) and (e==2)):          
                        print ('Draw')
                if ((c==2) and (e==3)):
                        j = j +1
                        print ('SG won this Round!!')
                if ((c==3) and (e==1)):
                        j = j +1
                        print ('SG won this Round!!')
                if ((c==3) and (e==2)):
                        h = h +1
                        print ('YOU won this Round!!')
                if ((c==3) and (e==3)):          
                        print ('Draw')
                print ()
                print ('SCORE => ',end="")
                print ('You = ',h,end='')
                print (' V/S SG = ',j)
                print('-----------------------------------------------------------')        
                #winning bolck
                l = i/2
                if (h>l):
                    print()
                    print ('Final Score => You = ',h , end='')
                    print (' V/S SG = ' , end= '' )
                    print (j)
                    print ('Final Result => YOU WON!!')
                    break 
                if (j>l):
                        print()
                        print ('Final Score => You = ',h , end='' )
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => YOU LOST...')
                        break
            if (h<l):
                        if (h>j):
                            print()
                            print ('Final Score => You = ',h, end='' )
                            print (' V/S SG = ' , end= '' )
                            print (j)
                            print ('Final Result => YOU WON!!')
            if (j<l):
                        if (j>h):
                            print()
                            print ('Final Score => You = ',h , end='')
                            print (' V/S SG = ' , end= '' )
                            print (j)
                            print ('Final Result => YOU LOST..')
            if (j==h):
                        print()
                        print ('Final Score => You = ',h ,end='' )
                        print (' V/S SG = ' , end= '' )
                        print (j)
                        print ('Final Result => DRAW!!')    
            print ()
            print ( 'Do you want to Quit??')
            print ()
            print('Enter 1 continue')
            print ('Enter 0 to quit')
            f =0
            while (f==0):
                    print ()
                    g = int(input ('Enter 1 or 0=> '))
                    if ((g==1) or (g==0)):
                        f= f+1
                    else:
                        print ('Invalid input, pls enter 0 or 1')
                        print()                   
            if (g==1):
                    a = a +1
            if (g==0):
                    a =a + 1
                    z = z +1
print ()
print ('Thank you for playing this Game!! ')
print ('Credits => SwarnabhG07' )
url = "https://www.instagram.com/swarnabhg07/?utm_source=qr"
print ('Follow My Insta Account => ',end ='')
print (url)    
print('====================================================================================================================')
m = input ('Press Enter to Quit Terminal..')
                        