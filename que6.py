# Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
#epts the number as an argument.n = int (input ("Enter a number: "))
factorial = 1
if n >= 1:
    for i in range (1, n+1):
        factorial=factorial *i
print("Factorial of the given number is: ", factorial)