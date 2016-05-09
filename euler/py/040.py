# champernowne's constant
strno = ''
for x in range(1,1000001): strno += str(x)
ans, n = int(strno[0]), ''

while len(n) < 6:
    n += '9'
    ans *= int(strno[int(n)])

print ans
