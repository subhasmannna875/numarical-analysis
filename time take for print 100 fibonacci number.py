""" 
    Python code for generating first 100 Fibonacci numbers.
    
    Python comes with a module called timeit. 
    I am using this module to calculate the execution time of this code.
"""

import fibonacci_module
import timeit


def main():
    n = 100  # Number of Fibonacci numbers to generate
    
    #Measure the execution time using timeit
    start_time = timeit.default_timer()
    fibonacci_numbers = fibonacci_module.generate_fibonacci(n)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
   


    print("First {} Fibonacci numbers:".format(n))

    print(fibonacci_numbers)

    print("\nExecution Time: {} seconds".format(execution_time))
    
    


if __name__ == "__main__":
    main()