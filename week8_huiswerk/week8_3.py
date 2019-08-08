#3.	1'den 1000'e kadar olan sayılardan mükemmel sayı olanları
#ekrana yazdırın. Bunun için bir sayının mükemmel olup
#olmadığını dönen bir tane fonksiyon yazın. Bir sayının,
#kendisi haric pozitif tam bolenleri toplami o sayiya
#esit ise mukemmel sayidir.
#Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28).


def perfectnum_generator(n):
    x = []
    
    for i in range (1, n):
        if n % i == 0:
            x.append(i)
    if sum(x) == n:
        print(n)
             
    else:
        pass

y = []
for n in range(1,1000):
    if perfectnum_generator(n) == n:
        y.append(n)
    else:
        pass


#a function where we type in a number
#and return bool True or False, if the number is
#a perfect number.

#Then we are to create another
#function that takes an upperlimit and will check
#every number up until that limit and if it is a
#perfect number, to print the perfect number.
#As of now my problem is with the 2nd half of
#this excersie, and instead of printing out
#the perfect number, it will print out how many
#there are with "True". Again the first function
#IS suppouse to return True or False, so I'm not sure
#how we can get the 2nd function to print out the actual number!


#def perfect(num):
#    x=1
#    adding=0
#    while x<num:
#        if num % x == 0:
#            adding=adding+x
#        x=x+1

#    if adding==num:
#        #print(num)
#        return (adding==num)
#    else:
#        return False
    
#def perfectList(upperlimit):
#    x=1
#    while x < upperlimit:
#        if perfect(x)==True:
#            print(x) # changed from print(perfect(x))
#        x=x+1

#print(perfectList(9))

##############PERFECT NUMBER GENERATOR THAT I WROTE###########
#def divisor_generator(n):
#    x = []
#    for i in range (1, n):
#        if n % i == 0:
#            x.append(i)
#    if sum(x) == n:
#        print( n, " is a perfect number.")
#    else:
#        print(n, " is not a perfect number.")
#        return x
    
#divisor_generator(28)


#eger sunu da eklersek o zaman 1den 1000e kadar tum sayilar icin tek tek bu perfect
#bu degil diye yazacak.
#for i in range(1,1000):
#    print(divisor_generator(i))
