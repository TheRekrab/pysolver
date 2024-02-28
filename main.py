from solver import PySolver

def linear(x):
    return 2*x + 2.5

def quadratic(x):
    return x**2 - 3 * x - 4

def main():
    psolver = PySolver.new() \
            .with_range((0, 10)) \
            .with_start_value(5) \
            .with_inc(1) \
            .with_function(quadratic)
    
    zero = psolver.find_zero()
    print(f"{zero}")

if __name__ == "__main__":
    main()
