# pythagorean triplets
# nice problem
def solutions(p):
    triplets=0
    for a in range(1,int(p/3)):
        if (p**2 - 2*a*p) % (2*p - 2*a) == 0: triplets+=1
    return triplets

max_p = max_sol = 0
for p in range(100,1001,2):
    sol = solutions(p)
    if sol > max_sol: max_sol,max_p = sol,p

print (max_p,max_sol)


    
    
        
                    


                    

            
