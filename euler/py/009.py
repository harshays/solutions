# a + b + c = 1000 pythagorean

ans = [a*b*int((a**2 + b**2)**0.5) for a in range(200,700) for b in range(a,700) if a + b + (a**2 + b**2)**0.5 == 1000.0 ]
print (ans[0])




