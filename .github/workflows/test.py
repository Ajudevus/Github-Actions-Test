import fact

def check_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    return fact

test="pass"
for i in range(1,10):
    if(fact.factorial(i)!=check_fact(i)):
        test="fail"

print(test)
    
    
