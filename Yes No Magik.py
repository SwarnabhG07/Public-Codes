import random
a=10
while (a<11):
    print ('------------------------------------------------------------')
    print ("ask any 'YES' or 'No' Ques ")
    print ()
    
    x = input ('Your Ques=> ')
    print ()
    n = random.randint(0,1)
    print ('Your Ans => ',end = '')
    if (n==0):
        print ('NO')
    if (n==1):
        print ('YES')
    print ()
    print ('Do you want to continue asking ques??')
    print ('enter 1 to continue , 0 to quit ')
    print ()
    h = int (input('enter 1 or 0 = > '))
    if (h==1):
              a = a +0
    if (h==0):
              a = a +1
print ()
print ('Thank you for playing this Game!! ')
print ('Credits => SwarnabhG07' )
url = "https://www.instagram.com/swarnabhg07/?utm_source=qr"
print ('Follow My Insta Account => ',end ='')
print (url)
print ('------------------------------------------------------------------')
              
          
        

