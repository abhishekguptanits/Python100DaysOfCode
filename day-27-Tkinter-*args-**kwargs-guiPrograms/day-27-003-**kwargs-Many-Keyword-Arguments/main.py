# def calculate(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# calculate(add=3, multiply=5)




def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
