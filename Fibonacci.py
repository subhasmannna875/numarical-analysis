def fibonacci(n):
    fib_seq = [0, 1]  # Initializing the sequence with the first two numbers: 0 and 1
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq[:n]  # Returning the first 'n' Fibonacci numbers

# Example: Generating the first 10 Fibonacci numbers
result = fibonacci(10)
print(result)
