def dist(n1, n2):
    return abs(n1 - n2)

class PySolver:

    def __init__(self):
        self.f = None
        self.upper_bound = None
        self.lower_bound = None
        self.start = None
        self.inc = None
        self.table = {}
        
        self.acceptable_error = 10 ** -4
        self.max_iterations = 10 ** 1 # 1 000 000 iterations = 1 million as default

    def new():
        self = PySolver()
        return self

    def verify(func):
        def wrapper(*args, **kwargs):
            self = args[0] # self is always first argument
            inputs = [self.f, self.upper_bound, self.lower_bound, self.start != None, self.inc, self.acceptable_error, self.max_iterations]
            if not all(inputs):
                print(inputs)
                raise Exception(f"PySolver instance was trying to run {func.__name__} without all inputs configured, exiting...")
            if self.lower_bound == self.upper_bound:
                raise Exception(f"PySolver instance had matching lower and upper bounds, leaving no room to travel: {self.lower_bound}")
            if self.lower_bound > self.upper_bound:
                raise Exception(f"PySolver instance had a lower bound that was greater than the upper bound: [{self.lower_bound}, {self.upper_bound}] in function: {func.__name__}")
            if self.start > self.upper_bound or self.start < self.lower_bound:
                raise Exception(f"PySolver instance has start set to {self.start} when the range was set to [{self.lower_bound}, {self.upper_bound}] in function {func.__name}")
            return func(*args, **kwargs)
        return wrapper
    
    def with_function(self, f):
        self.f = f
        return self

    def with_upper_bound(self, m):
        self.upper_bound = m
        return self

    def with_lower_bound(self, m):
        self.lower_bound = m
        return self

    def with_range(self, r):
        (self.lower_bound, self.upper_bound) = r
        return self

    def with_start_value(self, start):
        self.start = start
        return self

    def with_inc(self, inc):
        self.inc = inc
        return self

    def with_acceptable_error(self, e):
        self.acceptable_error = e
        return self
    
    def with_max_iterations(self, m):
        self.max_iterations = m
        return self
    
    @verify
    def get(self, n):
        if val := self.table.get(n):
            return val
        val = self.f(n)
        self.table[n] = val
        return val

    @verify
    def approach(self, goal):
        position = self.start
        val = self.get(position)
        inc = self.inc # we will make this smaller later to get close and closer to 0, somewhat like a binary search.
        d = dist(val, goal)
        diff  = val - goal

        iterations = 0

        while iterations <= self.max_iterations and d > self.acceptable_error:
            iterations += 1
            new_position = position + inc

            # verfify that we are still in our bounds, assuming that our original position is OK.
            if new_position == self.lower_bound or new_position == self.upper_bound:
                inc *= -0.5
                continue
            if new_position < self.lower_bound or new_position > self.upper_bound:
                # we may have to go slower, and try again.
                inc *= 0.5
                continue # none of the following code will execute this run. because it does not matter. 

            new_val = self.get(new_position)
            new_dist= dist(new_val, goal) # as we get closer, this number is positive. Negative number means we are getting further away than we were.
            gain = new_dist - old_dist
            new_diff = new_val - goal

            # have we crossed the line?
            if new_diff > 0 and diff < 0 or new_diff < 0 and diff > 0:
                # this means that we have overshot, so let's dial back our increments
                inc *= 0.5
            elif gain < 0:
                inc *= -1  # we are going the wrong way
            else:
                # this was a standard move (we got closer to the goal) SO: new_gain is positive, new_diff < diff
                # commit the move, and store the changes
                position = new_position
                val = new_val
                diff = new_diff


        return position, val

    def find_zero(self):
        return self.approach(0)

    def find_max(self):
        return self.approach(float("inf"))

    def find_min(self):
        return self.approach(-float("inf"))
