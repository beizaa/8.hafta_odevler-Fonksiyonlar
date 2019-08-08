#10.	Kullanıcıdan tire(-) ile ayrılan bir input dizisi
#alan ve sonrasında bu kelimeleri harf sırasına göre
#dizip tekrar tire ile ayırıp output olarak veren bir
#fonksiyon yazınız. örnek girdi: green-red-yellow-
#black-white örnek çıktı: black-green-red-white-yellow

a = input("Enter a sentence which are divided by - instead of spaces.")


def sorter(a):
    print(a.split("-"))
    sorted(a)
    str(a, sep="-")

print(sorter(a))
    
#calismiyor, uzerine calisacagim
