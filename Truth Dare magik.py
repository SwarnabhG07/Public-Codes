import random
import webbrowser
a=10
#Starting
while (a<11):
    print ('----------------------------------------------------------------------------------------')
    print ("Truth or Dare")
    print ()
    print ('Enter 1 for Truth')
    print ('Enter 0 for dare ')
    print ()
    b=11
#Input Block
    while (b<12):
        
        x = int(input ('Enter 1 or 0=> '))
        if (x>1):
            print ('Invalid input, pls enter 0 or 1')
            print ()
            b = b+ 0
        if ((x==1) or (x==0)):
                     b= b+1
#Code for 'Truth'    
    print ()
    if (x== 1):
        print ('Truth => ',end='')
        q = random.randint(0,17)
#All possible Truth Ques
        if (q==0):
            print ("Whats your GF's/Bf's name?? ")
        if (q==1):
            print ("Whats your Fav food ??")
        if (q== 2):
            print ("Whats your Dream place u like to visit??")
        if (q==3):
            print ("When was the last time you lied?")
        if (q== 4):
            print ('When was the last time you cried?')
        if( q==5):
            print ("What's your biggest fear?")
        if ( q==6 ):
            print ("What's your biggest fantasy?")
        if (q==7 ):
            print ("What's something you're glad your mum doesn't know about you?")
        if (q==8 ):
            print ("What's the worst thing you've ever done?")
        if (q==9):
            print ("What's a secret you've never told anyone?")
        if (q==10):
            print ("Do you have a hidden talent?")
        if (q==11):
            print ("Who was your first celebrity crush?")
        if (q==12):
            print ("Have you ever cheated in an exam?")
        if (q==13):
            print ("What's the most embarrassing thing you've ever done?")
        if (q==14):
            print ("What's the biggest mistake you've ever made?")
        if ( q==15 ):
            print ("Who would you like to kiss in this room?")
        if (q==16):
            print ("What's your worst habit?")
        if (q==17):
            print ("What's the most trouble you've been in?")
        print ()
        y = input ("Your Ans=> ")
        print()
#Code for "Dare"
    if (x==0):
        print ('Dare => ',end='')
        m = random.randint (0,21)
        if (m==0):
            print ("Slap the Person Near you")
        if (m==1):
            print ("Kill your Bestfriend ..")
        if (m==2):
            print ("Rob a Bank")
        if (m==3):
            print ("Show the most embarrassing photo on your phone")
        if (m==4):
            print ("Show the last five people you texted and what the messages said")
        if (m==5):
            print ("Eat a raw piece of garlic")
        if (m==6):
            print ("Do 100 squats")
        if (m==7):
            print ("Keep three ice cubes in your mouth until they melt")
        if (m==8):
            print ("Say something dirty to the person on your left")
        if (m==9):
            print ("Give a foot massage to the person on your right")
        if (m==10 ):
            print ("Yell out the first word that comes to your mind")
        if (m==11):
            print ("Eat a snack without using your hands")
        if (m==12):
            print ("Say two honest things about everyone else in the group")
        if (m==13):
            print ("Twerk for a minute")
        if (m==14):
            print ("Try and make the group laugh as quickly as possible")
        if (m==15):
            print ("Try to put your whole fist in your mouth")
        if (m==16):
            print ("Try to lick your elbow")
        if (m==17):
            print ("Howl like a wolf for two minutes")
        if (m==18):
            print ("Dance without music for two minutes")
        if (m==19):
            print ("Pole dance with an imaginary pole")
        if (m==20):
            print ("Let someone else tickle you and try not to laugh")
        if (m==21):
            print ("Put as many snacks into your mouth at once as you can")

        print()
#End of game        
    print ('Do you want to continue Playing??')
    print ('Enter 1 to continue , 0 to quit ')
    print ()
    c=9    
#Quitting Block
    while (c<10):
            h = int(input ('Enter 1 or 0=> '))
            if (h>1):
                print ('Invalid input, pls enter 0 or 1')
                print()
                c = c+ 0
            if ((h==1) or (h==0)):
                     c= b+1
                     
    if (h==1):
              a = a +0
    if (h==0):
              a = a +1
    print ()
#Outro
print()
print ('Thank you for playing this Game!! ')
print ('Credits => SwarnabhG07' )
url =  "https://youtu.be/LKeW-bcl1p8"
webbrowser.open_new(url)
print ('------------------------------------------------------------------')

