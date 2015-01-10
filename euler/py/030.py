# num = sum of fifth pow of digits
def fifpow(n): return sum(map(lambda x: int(x)**5,str(n)))
for i in range(1,999999+1):
    if i == fifpow(i): print (i)

