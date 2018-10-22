# Recursion needs a number of bases and
# one or more recursive cases which are
# defined using definition of function being defined
def factorial(n):
    # return 1 if n = 0
    # return n * (n - 1)! if n >= 0
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
