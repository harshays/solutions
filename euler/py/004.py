# max palindrome
ans = max([i*j for i in range(100,1000) for j in range(i,1000) if str(i*j) == str(i*j)[::-1]])
print (ans)
