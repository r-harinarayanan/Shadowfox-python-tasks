# Creating a variable named pi and storing the value 22/7 in it.
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))  # This shows the data type

# trying to use 'for' as a variable name and see what happens
try:
    exec("for = 4")  # You can't use reserved keywords like 'for'
except SyntaxError:
    print("You can't use 'for' as a variable name because it's a reserved keyword.")

# Simple Interest calculation
P = 1000  # Principal amount
R = 5     # Rate of interest
T = 3     # Time in years
SI = (P * R * T) / 100
print("Simple Interest is:", SI)
# In the above code, the task specifically required the values to be entered manually instead of asking the user for input.