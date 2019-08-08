#1.	Asal sayi olup olmadigini kontrol eden fonksiyon yazınız

def prime_num_control(x):
    while True:
        counter = 0
        
        for i in range(2,int(x)):
            if int(x) % i == 0:
                counter += 1
                if counter != 0:
                    print(x, "is a not prime number.")

                else:
                    print(x, "is a prime number.")
        break
    
prime_num_control(15)

#yaptim ama hatali, output hic durmadan veriliyor


