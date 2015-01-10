# score of names.

name_file=open("input/22input.txt",'r').read()
names = sorted(list(map(lambda x: x[1:-1],name_file.split(','))))

abc={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11, 'L':12,'M':13,'N':14,
    'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
total_score = 0
for name in names:
    score = 0
    for letter in name: score += abc[letter]
    score *= (names.index(name)+1)
    total_score += score
    
    
        
print (total_score)
