# total of all palindromes in base 10 and 2

def tobinary(n): return str(bin(n))[2:]
def palindrome(n): return str(n) == str(n)[::-1]
total = 0
for n in range(1,1000000):
    if palindrome(n) and palindrome(tobinary(n)): total += n
print (total)