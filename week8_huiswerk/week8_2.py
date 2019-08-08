#2.	Bir sayinin tam bolenlerini bulan fonksiyon yazınız.



def divisor_generator(n):
    x = []
    for i in range (1, n+1):
        if n % i == 0:
            x.append(i)
    return x

print(divisor_generator(20))

#def divisorGenerator(n):
#    for i in xrange(1,n/2+1):
#        if n%i == 0: yield i
#    yield n

#print(divisorGenerator(12))

#def divisorGen(n):
#    factors = list(factorGenerator(n))
#    nfactors = len(factors)
#    f = [0] * nfactors
#    while True:
#        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
#        i = 0
#        while True:
#            f[i] += 1
#            if f[i] <= factors[i][1]:
#                break
#            f[i] = 0
#            i += 1
#            if i >= nfactors:
#                return
#print(divisorGen(12))


