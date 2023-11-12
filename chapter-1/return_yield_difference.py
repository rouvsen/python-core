
def foo1(x):
    counter = 0
    for i in range(x + 1):
        counter += i
    return counter

print(foo1(10))

print("************")

def foo2(x):
    counter = 0
    for i in range(x + 1):
        counter += i
        yield counter

for el in foo2(10):
    print(el)