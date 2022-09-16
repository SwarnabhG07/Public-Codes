v=2
while (v<3):
    print ('__________________________________________________________________________')
    print ('Find Roots of any Quadratic Equation')
    print ()
    print ('Format = ax^2 + b x + c = 0')
    print ('a = coeffiecient of x^2')
    print ('b = coeffiecient of x')
    print ('c = constant term')
    print ()
    a = int ( input ('a='))
    b= int ( input ('b='))
    c = int ( input ('c='))
    print ()
    if (a==0):
        print ('invalid , a cannot be zero')
    else:
        print ('Your Equation => ' ,a,'x^2 + ' ,b,'x + ', c, ' = 0')
    print ()

    D = b**2 - (4*a*c)
    if (D<0) :
       print('No real roots')
    else:
          n = (-b + (D ** (1/2)))/2*a
          m = (-b - (D ** (1/2)))/2*a
          print  ('x =',m ,'or x=',n)
    print ()
    print ('Do you want to calculate more ??')
    print ()
    print ('Enter 1 to continue')
    print ('Enter 0 to Quit Module')
    print ()
    g = 9
    while (g<10):
            h = int(input ('Enter 1 or 0=> '))
            if (h>1):
                print ('Invalid input, pls enter 0 or 1')
                print()
                g = g+ 0
            if ((h==1) or (h==0)):
                     g= g+1
                     
    if (h==1):
              v = v +0
    if (h==0):
              v = v +1
print ()
print ('Thank you for Using this Program!!')
print ('Credits => SwarnabhG07' )
print ()
url = "https://www.instagram.com/swarnabhg07/?utm_source=qr"
print ('Follow My Insta Account => ',end ='')
print (url)
print ('__________________________________________________________________________')
# credits - @SwarnabhG07 (instagram)





