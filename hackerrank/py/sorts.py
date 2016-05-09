import random
import timeit
import profile

def randomarray(L,r=1000): return [random.randint(1,r) for x in range(L)]

def insertion_sort(a): #iteration
	for x in range(1,len(a)):
		key = a[x]
		prev = x - 1
		while (prev >= 0) and (a[prev] > key):
			a[prev+1]=a[prev]
			prev -= 1
		a[prev+1] = key
	return a

def insertion_sort_rec(a,index): # a should be sorted
	if index == 0: return a
	insertion_sort_rec(a,index-1)
	j = index
	while j > 0 and a[j-1] > a[j]:
		a[j-1],a[j] = a[j],a[j-1]
		j-=1
	return a

def selection_sort(a):
	l = len(a)
	for i in range(l-1,0,-1):
		max_j = i
		for x in range(i):
			if a[x] > a[max_j]: max_j = x
		a[i],a[max_j] = a[max_j],a[i]

def selectionsort_rec(a):
	def recurse_sort(a,ind):
		if ind == 0: return a
		temp_max = max(a[:ind])
		max_index = a.index(temp_max)
		a[ind],a[max_index]=a[max_index],a[ind]
		return recurse_sort(a,ind-1)
	return recurse_sort(a,len(a)-1)

def selectionsort_pythonic(a):
	l = len(a)
	for i in range(l-1,0,-1):
		temp_max = max(a[:i])
		max_index = a.index(temp_max)
		a[i],a[max_index]=a[max_index],a[i]
	return a
	
def quicksort(a): #recursive
	if len(a) == 0 or len(a) == 1: return a
	if len(a) == 2: return [min(a),max(a)]
	while len(a) > 2:
		p = a[0]
		same = len(list(filter(lambda x: x == p, a)))
		less = list(filter(lambda x: x < p, a))
		great = list(filter(lambda x: x > p, a))
		return (quicksort(less) + [p]*same + quicksort(great))

def bs_rec(lst,key):
	def rec(lst,key,st,en):
		if en < st: return -1
		mid = (en + st)//2
		if key == lst[mid]: return mid
		elif key < lst[mid]: return rec(lst,key,st,mid-1)
		else: return rec(lst,key,mid+1,en)
	return rec(sorted(lst),key,0,len(lst)-1)

def binary_search(lst,key):
	lst = sorted(lst)
	st,en = 0,len(lst)-1
	while en >= st:
		mid = (en + st)//2
		if key == lst[mid]: return mid
		elif key < lst[mid]:
			en = mid - 1
		else: 
			st = mid + 1
	return -1

def shuffle_knuth(a):
	l = len(a)
	for x in range(l):
		random_index = random.randint(0,l-1)
		print (x,random_index)
		a[random_index],a[x] = a[x],a[random_index]
	return a

# testing
if __name__ == '__main__':
	pass

