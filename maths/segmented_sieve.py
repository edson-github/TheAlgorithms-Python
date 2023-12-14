import math

def sieve(n):
    in_prime = []
    end   = int(math.sqrt(n)) # Size of every segment
    temp = [True] * (end + 1)
    prime = []

    for start in range(2, end + 1):
        if temp[start] == True:
            in_prime.append(start)
            for i in range(start**2, end+1, start):
                if temp[i] == True:
                    temp[i] = False
    prime += in_prime

    low = end + 1
    high = low + end - 1
    high = min(high, n)
    while (low <= n):
        temp = [True] * (high-low+1)
        for each in in_prime:

            t = math.floor(low / each) * each
            if t < low:
                t += each

            for j in range(t, high+1, each):
                temp[j - low] = False

        for j in range(len(temp)):
            if temp[j] == True:
                prime.append(j+low)

        low = high + 1
        high = low + end - 1
        high = min(high, n)
    return prime

print(sieve(10**6))