import time
import matplotlib.pyplot as plt

# Function to calculate Fibonacci number iteratively
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Function to calculate Fibonacci number recursively
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to measure execution time
def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

# Define the input sizes for testing
input_sizes = [5, 10, 15, 20, 25, 30, 35]
iterative_times = []
recursive_times = []

# Measure execution times for each method and input size
for size in input_sizes:
    iterative_times.append(measure_time(fibonacci_iterative, size))
    recursive_times.append(measure_time(fibonacci_recursive, size))

# Calculate Fibonacci numbers for 12 months
n_months = 12
rabbit_pairs_iterative = fibonacci_iterative(n_months)
rabbit_pairs_recursive = fibonacci_recursive(n_months)

# Print the results
print(f"Number of rabbit pairs after {n_months} months (Iterative): {rabbit_pairs_iterative}")
print(f"Number of rabbit pairs after {n_months} months (Recursive): {rabbit_pairs_recursive}")

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, iterative_times, label='Iterative', marker='o')
plt.plot(input_sizes, recursive_times, label='Recursive', marker='o')

plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Fibonacci Calculation')
plt.legend()
plt.grid(True)

plt.show()
