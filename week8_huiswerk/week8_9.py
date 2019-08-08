#9.	Kullanıcıdan bir input alan ve bu inputun içindeki
#büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.

word = input("""Enter a word or text that you want to
             calculate its small and capital letters: """)

def up_low_calc(word):
    x = []
    y = []
    for i in word:
        if i.isupper() == True:
            x.append(i)
            
        elif i.islower() == True:
            y.append(i)

        else:
            pass
    print("There are", len(x), "capital and ", len(y), "small letters in this text.")
    return len(x)
    return len(y)
    
    
        
up_low_calc(word)

            
