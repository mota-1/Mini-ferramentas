import math
def equation(x):
    return math.gamma(x) - (x**2 - 1)

def find_solution():
    # Initial values for the bisection method
    a = 1.0
    b = 3.0

    while b - a > 1e-15:  # Continue until the desired level of precision is reached
        
        mid = (a + b) / 2
        if equation(a) * equation(mid) < 0:
            b = mid
        else:
            a = mid

    return (a + b) / 2

solution = find_solution()
print(solution)