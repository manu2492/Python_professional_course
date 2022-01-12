def make_multiplier(x):

    def multiplier(n):

        return x * n

    return multiplier

times3 = make_multiplier(3)

print(times3(5))



