
# Set values for s - sides of regular dice, n - total number of dices.
s = 6
n = 6

from sympy import symbols, expand
import matplotlib.pyplot as plt

def compute_combinations(s, n):
    x = symbols('x')
    expression = sum(x**n for n in range(s))
    # combinations list as coefficients of polynomial function:
    combinations_list = expand(expression**n).as_poly(x).all_coeffs()
    return combinations_list
    print(combinations)

# General equation for regural sided s dice and n - total number of  dices are:
# combinations = (1 + x)**n                                  - for 2-sided dice (coin) and for n - coins is Biniomial theorem to get coefficients (Galton Board) and (Pascal Triangle).
# combinations = (1 + x + x**2 + x**3 +...+ x**(s-1) )**n    - for s-sided regular dice and n - total number of dices to get coefficients. 

# # Compute the combinations for the chosen values of s and n
combinations= compute_combinations(s, n)
print()
print('Sequence of combinations =', combinations)

# Plotting the combinations
x_values = list(range(n, s * n + 1))  # x-axis values starting from n
plt.bar(x_values, combinations)

# # Compute the sum, max, and mean
sum_of_combinations = sum(combinations)
max_of_combinations = max(combinations)
mean_of_combinations = (n + (s * n)) / 2

print()
print("Sum of totat combinations are s**n =", sum_of_combinations)
print('Max probability=', float(max_of_combinations / s**n))
print('Mean dice sum =', int(mean_of_combinations))

# Plotting the dashed symmetry line for mean value
plt.axvline(x= mean_of_combinations, color='r', linestyle='--', label='Mean')
plt.text(mean_of_combinations, max(combinations), f'Mean = {mean_of_combinations}', va='bottom', ha='center')

# Set tick labels for every second x-axis value starting from initial to max:
plt.xticks(range(n, s * n + 1, 3))

plt.xlabel('Value of n')
plt.ylabel('Combinations')
plt.title('Combinations from dice number of n')
plt.legend()
plt.show()




