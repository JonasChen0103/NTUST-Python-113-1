def get_total(N):
    return sum(range(1, N + 1))

def get_factorial(N):
    if N == 0:
        return 1

    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    return factorial

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def main():
    # Print Department_Student ID_Name.
    print("資工一_B11315013_陳皓岳")

    # Enter an positive integer N from the keyboard and display the number on the screen.
    N = int(input("Enter a positive integer N: "))
    print(f"N = {N}")

    # Calculate 1+2+…+N and display the result on the screen.
    total_sum = get_total(N)
    output = ""

    for i in range(1, total_sum, 1):
        output += str(i) + "+"

    print(f"{output}{N}={total_sum}")

    # Calculate N! (N-factorial) and display the result on the screen.
    factorial = get_factorial(N)
    print(f"{N}! = {factorial}")

    # Determine whether N is a prime number and display the result on the screen.
    if is_prime(N):
        print(f"{N} 是質數 ({N} is a prime number.)")
    else:
        print(f"{N} 不是質數 (is not a prime number.)")

if __name__ == "__main__":
    main()
