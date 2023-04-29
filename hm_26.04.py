def tail(test, n):
    with open(test) as f:
        return '\n'.join(f.readlines()[-n:])

print(tail('test.txt', 5))

