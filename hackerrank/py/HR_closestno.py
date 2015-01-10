N = int(input())
def makelistsameline(strnos): return list(map(lambda x: int(x),strnos.split()))
a = makelistsameline(input())
a.sort()