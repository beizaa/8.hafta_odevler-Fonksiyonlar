#11.	Verilen bir listenin içindeki özgün elemanları
#ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
#Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]

list1 = [22, 22, 33, 33, 44, 44, 56, 56, 78, 78, 90, 90, 23, 23, 23, 34, 91, 91, 93, 99, 99]

def unique_list(l):
    x = []
    for a in l :
        if a not in x :
            x.append(a)
    return x

print(unique_list( list1 ))
