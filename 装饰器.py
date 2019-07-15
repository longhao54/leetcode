#
#
# def test1(func):
#     print("haha")
#     def test2(*args):
#         print(1)
#         a = func(*args)
#         print(2)
#         return a
#     return test2
#
# @test1
# def test3(x):
#     print(f"{x} hahaha")
#
#
# print(test3.__name__)



# def decorator_a(func):
#     print('Get in decorator_a')
#     def inner_a(*args, **kwargs):
#         print('Get in inner_a')
#         return func(*args, **kwargs)
#     print(func.__name__,"a")
#     return inner_a
#
# def decorator_b(func):
#     print('Get in decorator_b')
#     def inner_b(*args, **kwargs):
#         print('Get in inner_b')
#         return func(*args, **kwargs)
#     print(func.__name__,"b")
#     return inner_b
#
# @decorator_b
# @decorator_a
# def f(x):
#     print('Get in f')
#     return x * 2
#
# print(f.__name__)
# f(1)



def test(ak=1):
    def test1(func):
        print("haha")
        def test2(*args):
            print(1)
            a = func(*args)
            print(2)
            return a
        return test2
    return test1

@test(2)
def test3(x):
    print(f"{x} hahaha")


print(test3.__name__)



