# Nth Fibonacci The Fibonacci sequence is defined as follows: the first number
# of the sequence is 0, the second number is 1, and the nth number
# is the sum of the (n-1)th and (n-2)th numbers. Write a function that takes
# an integer n and returns the nth Fibonacci number

def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

if __name__ == '__main__':
    print("N =", 5, "Answer is:", getNthFib(5))
    print("N =", 6, "Answer is:", getNthFib(6))
    print("N =", 18, "Answer is:", getNthFib(18))

