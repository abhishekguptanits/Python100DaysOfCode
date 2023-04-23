def add(*args):
    print(args)
    print(type(args))
    result = 0
    for n in args:
        result += n
    return result


total_sum = add(1, 2, 3)
print(total_sum)
