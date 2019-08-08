#4.	Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük
#ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

print(" THE GREATEST COMMON DIVISOR ")
print("Please enter the small value first.")  #burada a > < b vs yapilabilirdi de boyle daha kolay lol
e = int(input("Enter the first value: "))
f = int(input("Enter the second value: "))

def greatest_common_div(a, b):
    x = []
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            x.append(i)
    sorted(x)
    return x[-1]
    print(x[-1])

print(greatest_common_div(e, f))

    
