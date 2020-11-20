# 45*32 = 40*2+40*30+5*2+5*30
from timeit import default_timer as timer

a = 45
b = 32


def grade_multiply(num1, num2):
    product = 0
    num1_len = len(str(num1))
    num2_len = len(str(num1))
    for i1, n1 in enumerate(str(num1), 1):
        for i2, n2 in enumerate(str(num2), 1):
            product += (int(n1) * 10**(num1_len - i1)) * (int(n2) *
                                                          10**(num2_len - i2))
    return product


start = timer()
waka = grade_multiply(a, b)
end = timer()
print('*' * 5)
print(waka)
print(end - start)

start = timer()
waka = a * b
end = timer()
print('*' * 5)
print(waka)
print(end - start)