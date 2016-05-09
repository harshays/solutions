# maximum path sum I
f = open('input/18input.txt').read().split('\n')
for x in range(len(f)):
	f[x] = list(map(int,f[x].split()))

row_now = len(f) - 2 # second last

while row_now >= 0:
	row_down = row_now + 1
	for ind in range(len(f[row_now])): f[row_now][ind] += max(f[row_down][ind],f[row_down][ind+1])
	row_now -= 1

print (f[0][0]) # max sum.

