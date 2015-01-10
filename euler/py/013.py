# first ten digits of sum
f = open('input/13input.txt').read().split('\n')
f = str(sum(map(int,f)))
print (f[:10])