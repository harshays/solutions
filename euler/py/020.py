# sum of digits of 100!
p,s=1,0
for i in range(2,101): p*=i
for i in str(p): s+=int(i)
print (s)
    
    
