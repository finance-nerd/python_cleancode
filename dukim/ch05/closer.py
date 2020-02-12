def circumference(radius):
    """ closer example """

    def calculate(pi):
        return radius * radius * pi

    return calculate


c = circumference(10)
print(c(3.14))
print(c(3.1415))
