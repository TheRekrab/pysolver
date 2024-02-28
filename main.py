from solver import PySolver
import math

def linear(x):
    return 2*x + 2.5

def quadratic(x):
    return -1 * x**2 + x

def weird(x):
    return math.sin(x) + math.cos(x)

def main():
    psolver = PySolver.new() \
            .with_range((0, 5)) \
            .with_start_value(2.5) \
            .with_inc(1) \
            .with_function(weird)
    
    point = psolver.find_max()
    print(f"{point}")

if __name__ == "__main__":
    main()
