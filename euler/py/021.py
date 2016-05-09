# amicable numbers
def div(n): return sum([i for i in range(1,(n//2)+1) if n % i == 0])

amis = set()
for i in range(1,10000):
    d1 = div(i)
    d2 = div(d1)
    if i == d2 and d1 != d2:
        amis.add(d1)
        amis.add(d2)

print (sum(amis))