import numpy as np
import matplotlib.pyplot as plt
import random

def polynomial_function(x):
    
    return x**3 - 2*x - 5

def bisection_method(func, a, b, tolerance=1e-7, max_iterations=100):
   
    if func(a) * func(b) >= 0:
        print("Error: Function values at the interval endpoints must have opposite signs.")
        return None, np.array([[a, b]])

    updates = np.array([[a, b]])
    for _ in range(max_iterations):
        mid = (a + b) / 2
        updates = np.vstack([updates, [a, b]]) 
        if abs(func(mid)) < tolerance or (b - a) / 2 < tolerance:
            return mid, updates

        if func(mid) * func(a) < 0:
            b = mid
        else:
            a = mid

    print("Warning: Maximum iterations reached. The root might not be within the desired tolerance.")
    return (a + b) / 2, updates

def find_initial_interval(func, search_range=[-10, 10], num_probes=100):
   
    x_values = np.linspace(search_range[0], search_range[1], num_probes)
    random.shuffle(x_values)

    for i in range(num_probes - 1):
        a = x_values[i]
        b = x_values[i+1]
        if func(a) * func(b) < 0:
            return [min(a, b), max(a, b)]

    print(f"Warning: Could not find an initial interval with opposite signs after {num_probes} probes in the range {search_range}.")
    return None

if _name_ == "_main_":
    f = polynomial_function

    
    initial_interval = find_initial_interval(f)

    if initial_interval:
        a_initial, b_initial = initial_interval
        print(f"Initial interval found: [{a_initial:.4f}, {b_initial:.4f}]")

       
        root, updates = bisection_method(f, a_initial, b_initial)

        if root is not None:
            print(f"Approximate root found: {root:.8f}")

            
            plt.figure(figsize=(10, 6))

           
            x_plot = np.linspace(updates[0, 0] - 1, updates[0, 1] + 1, 400)
            y_plot = f(x_plot)
            plt.plot(x_plot, y_plot, label='f(x)')
            plt.axhline(0, color='black', linewidth=0.8, linestyle='--', label='y=0')

            
            for i in range(updates.shape[0]):
                a_i, b_i = updates[i]
                mid_i = (a_i + b_i) / 2
                plt.plot([a_i, b_i], [f(a_i), f(b_i)], 'r-', alpha=0.5, label='Interval' if i == 0 else "")
                plt.plot(mid_i, f(mid_i), 'go', markersize=5, label='Midpoint' if i == 0 else "")

            plt.plot(root, f(root), 'b*', markersize=10, label='Approximate Root')

            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Bisection Method for Root Finding')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("Bisection method failed to find a root within the given parameters.")
    else:
        print("Could not find a suitable initial interval for the bisection method.")
