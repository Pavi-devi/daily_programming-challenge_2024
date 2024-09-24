import math

def find_lcm(N, M):
    gcd = math.gcd(N, M)
    lcm = (N * M) // gcd
    return lcm

N = 4
M = 6
print(find_lcm(N, M))  
