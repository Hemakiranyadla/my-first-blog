def sum():
    def sum2():
        c = 1+2
        return c
    return sum2

def sum_test():
    def sum2_test():
        c = 1+2
        return c
    return sum2_test

def fun_func(out_more):
    out = out_more()
    return "harsha"+out

def fun():
    return "Welcome"

a = sum()
print(a)