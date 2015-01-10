# number score. trivial.
sing={'1':3,'2':3,'3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4,'10':3,'11':6,'12':6,
    '13':8,'14':8,'15':7,'16':7,'17':9,'18':8,'19':8,'20':6,'30':6,'40':5,'50':5,'60':5,
    '70':7,'80':6,'90':6}
tens={'1':3,'2':6,'3':6,'4':5,'5':5,'6':5,'7':7,'8':6,'9':6}
teens={'1':6,'2':6,'3':8,'4':8,'5':7,'6':7,'7':9,'8':8,'9':8}

def make(no):
    n=str(no)
    if len(n) == 1: return sing[n]
    elif len(n) == 2:
        if n[-1] is '0': return sing[n]
        elif n[0] is '1': return sing[n]
        elif int(n[0]) > 1 and n[-1] is not '0': return tens[n[0]] + sing[n[1]]
    elif len(n) == 3:
        if n[-1] is '0' and n[-2] is '0': return sing[n[0]]+7 #300
        elif n[-1] is '0' and n[-2] is not '0': return sing[n[0]]+10+tens[n[-2]] #450 
        elif n[-1] is not '0' and n[-2] is '0': return sing[n[0]]+10+sing[n[-1]] #409
        elif n[-1] is not '0' and int(n[-2]) > 1: return sing[n[0]]+10+tens[n[1]]+sing[n[2]] #456
        elif n[-1] is not '0' and n[-2] is '1': return sing[n[0]]+10+teens[n[-1]]
    elif len(n) == 4: return 11

total=0
for i in range(1,1001): total+=make(i)
print (total)

