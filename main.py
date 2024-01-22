#### About args ####

# *args (Positional Arguments):
#
# *args allows a function to accept any number of positional arguments.
# The asterisk (*) before "args" allows you to pass a variable number of positional arguments to the function.
# The values passed as positional arguments are collected into a tuple.


### About kwargs ####


# **kwargs allows a function to accept any number of keyword arguments.
# The double asterisk (**) before "kwargs" allows you to pass a variable number of keyword arguments to the function.
# The values passed as keyword arguments are collected into a dictionary.


###  args

def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


sum(1, 3, 5)

### kwargs


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(kwargs["hi"])
    n += kwargs["hi"]
    n *= kwargs["hlo"]
    print(n)


calculate(n=1, hi=11, hlo=22)


# #### practice

#####  *args   #####

def minu(*args):
    main = 100
    for i in args:
        main -= i
    print(main)


minu(1, 2, 3, 4)


######  **kwargs #####3


def calculations(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        print(n)
        n += kwargs["sum"]
        n -= kwargs["minu"]


calculations(66, sum=12, minu=2)


def add(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)


add(1, 2, 3, 4, 5)


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(kwargs["name"])


print_address(name="srjan", Hm="Sircilla", cur="HYD")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for key, value in kwargs.items():
        print(kwargs.get("street"))

