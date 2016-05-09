# even fibo sum
seq = [1,2]
while seq[-1] < 4000000:
    seq.append(seq[-1]+seq[-2])
seq = sum(filter(lambda x: x%2 == 0, seq))
print (seq)