import math
n = int(input("Enter n: "))

def sieve(n):
    l = [True] * (n+1)
    prime = []
    end   = int(math.sqrt(n))
    for start in range(2, end + 1):
        if l[start] == True:
            prime.append(start)
            for i in range(start**2, n+1, start):
                if l[i] == True:
                    l[i] = False
    prime.extend(j for j in range(end+1,n+1) if l[j] == True)
    return prime

print(sieve(n))
        
