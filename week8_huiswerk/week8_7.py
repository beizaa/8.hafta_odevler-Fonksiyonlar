#7.	1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
#ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)


a =  in range(1, 101)
b =  in range(1, 101)
c =  in range(1, 101)
def pisagor_triangle(a, b, c):
    x = []
    for i in range(1, 101):
        if pow(a, 2) + pow(b, 2) == pow(c, 2):
            print(a, "-", b, "-", c, "triangle")
        else:
            pass
    
pisagor_triangle(a, b, c)

#calismiyor, tamamlayacagim ins
