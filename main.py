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

