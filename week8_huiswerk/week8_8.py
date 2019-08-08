#8.	Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n=int(input("Enter a number that you want its factiorial : "))

print(factorial(n))
