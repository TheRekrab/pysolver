from solver import PySolver

def linear(x):
    return 2*x + 2

def main():
    psolver = PySolver.new() \
            .with_range((-10, 10)) \
            .with_start_value(0) \
            .with_inc(1) \
            .with_function(linear)
    
    zero = psolver.find_zero()
    print(f"{zero}")

if __name__ == "__main__":
    main()
