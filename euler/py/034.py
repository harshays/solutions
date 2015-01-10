# sum of digital factorial equal to number
cache = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

def check(no):
    ans = sum(list(map(lambda x: cache[int(x)],str(number))))
    return no == ans

for i in range(2,9999999):
    if check(i): print (i)

