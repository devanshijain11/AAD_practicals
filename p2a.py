import time
import matplotlib.pyplot as plt
import sys

# Increase the recursion limit for large inputs
sys.setrecursionlimit(1000000)

# Function to calculate sum using a loop
def sum_using_loop(N):
    total = 0
    for i in range(1, N + 1):
        total += i
    return total

# Function to calculate sum using the formula
def sum_using_equation(N):
    return N * (N + 1) // 2

# Function to calculate sum using recursion
def sum_using_recursion(N):
    if N == 1:
        return 1
    return N + sum_using_recursion(N - 1)

# Function to measure execution time
def measure_time(func, N):
    start_time = time.time()
    try:
        func(N)
    except RecursionError:
        return float('inf')
    end_time = time.time()
    return end_time - start_time

# Define the input sizes for testing
input_sizes = [100, 1000, 5000, 10000, 20000, 50000, 100000]
loop_times = []
equation_times = []
recursion_times = []

# Measure execution times for each method and input size
for size in input_sizes:
    loop_times.append(measure_time(sum_using_loop, size))
    equation_times.append(measure_time(sum_using_equation, size))
    recursion_times.append(measure_time(sum_using_recursion, size))

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, loop_times, label='Loop', marker='o')
plt.plot(input_sizes, equation_times, label='Equation', marker='o')
plt.plot(input_sizes, recursion_times, label='Recursion', marker='o')

plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time for Sum of 1 to N')
plt.legend()
plt.grid(True)
plt.show()
