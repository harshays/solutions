# coded triangular numbers

abc={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
    'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

trino=set()
for i in range(1,10000): trino.add((i**2 + i)/2)

def name_score(word):
    score = 0
    for letter in word: score += abc[letter]
    return score 

words_input=open("input/42input.txt",'r').read()
words = list(filter(lambda x: x in trino, (map(lambda x: name_score(x),map(lambda x: x[1:-1],words_input.split(','))))))
print (len(words))






    
    
   