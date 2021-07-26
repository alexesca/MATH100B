def factorization(n):
    i = 1
    factors = []
    while i <= n:
        reminder = n % i
        is_factor = reminder == 0  # To "divide evenly" means that one number can be divided by another without anything left over. In other words no remainder!
        print("Case: ", n, " / ", i, " Module operation result: ", reminder, "Is factor?", is_factor)
        if is_factor:
            factors.append(i)
        i += 1
    print("Factors of", n, factors)


factorization(15)
