def prime_factorization(N):
    if N < 1:
        raise ValueError("Input must be a positive integer.")
    
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i

    if N > 2:
        factors.append(N)
    
    return factors

def main():
    try:
        number = int(input("Enter a positive integer: "))
        result = prime_factorization(number)
        print(f"Prime factorization of {number}: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Execute the main function
if _name_ == "_main_":
    main()
