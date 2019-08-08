#5.	Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük
#ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

print(" THE LEAST COMMON MULTIPLER ")
print("Please enter the small value first.")  #burada a > < b vs yapilabilirdi de boyle daha kolay lol
e = int(input("Enter the first value: "))
f = int(input("Enter the second value: "))

def least_common_mult(a, b):
    x = []
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            x.append(i)
    sorted(x)
    return x[1]
    print(x[1])

print(least_common_mult(e, f))
