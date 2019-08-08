#12.	Verilen inputların tersten de aynı olup
#olmadığını kontrol eden bir fonksiyon yazınız.
#örnek: madam, taco cat, utrecht sonuç: True, True, False

#PALINDROMES
#function of words that spelt same in forward and backwards in python

def palindrome_checker(a):
    if list(a) == list(reversed(list(a))):
        print(a, " is a palindrome.")
    else:
        print(a, " is not a palindrome.")
    return a

palindrome_checker("babab")
