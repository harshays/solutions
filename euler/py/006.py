# sum of sq minus sq of sum
ss=[x**2 for x in range(1,101)]
sq=((100*101)/2)**2
print (int(sq-sum(ss)))
