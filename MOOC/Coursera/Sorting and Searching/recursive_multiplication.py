# x = 4
# print('x: {}'.format(x))

# str_x = str(x)
# print('str x: {}'.format(str_x))

# len_x = len(str_x)
# print('len x: {}'.format(len_x))

# mid = len_x // 2
# print('mid x: {}'.format(mid))

# a = int(str_x[:mid])
# print('a: {}'.format(a))

# b = int(str_x[mid:])
# print('b: {}'.format(b))

# full_x = 10**(len_x / 2) * a + b
# print('full x: {}'.format(full_x))

def recursive_mult(x, y):
    str_x = str(x)
    len_x = len(str_x)
    str_y = str(y)
    len_y = len(str_y)

    if len_y == 1 or len_x == 1:
        return x * y

    x_mid = len_x // 2
    a, b = int(str_x[:x_mid]), int(str_x[x_mid:])
    print('a: {}, b: {}'.format(a, b))

    y_mid = len_y // 2
    c, d = int(str_y[:y_mid]), int(str_x[y_mid:])
    print('c: {}, d: {}'.format(c, d))

    print(str_x, len_x, x_mid)
    print(str_y, len_y, y_mid)

    print('***')
    ac = a * c
    # ac = recursive_mult(a, c)
    print('ac ({} * {}): {}'.format(a, c, ac))
    ad = a * d
    # ad = recursive_mult(a, d)
    print('ad ({} * {}): {}'.format(a, d, ad))
    bc = b * c
    # bc = recursive_mult(b, c)
    print('bc ({} * {}): {}'.format(b, c, bc))
    # bd = recursive_mult(b, d)
    bd = b * d
    print('bd ({} * {}): {}'.format(b, d, bd))

    result = (10**(len_x / 2)) * (10**(len_y / 2)) * ac + 10**(
        len_x / 2) * ad + 10**(len_y / 2) * bc + bd
    return result

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627
# waka = recursive_mult(num1, num2)
waka = num1*num2
print('*' * 5)
print(int(waka))
# Correct
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184