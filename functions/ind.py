# def sum_num(a, b):
#     return a * b


# x = sum_num(10, 32)
# print(x)


# def is_hello_in_text(text):
#     if "hello" in text:
#         return True
#     else:
#         return False


# print(is_hello_in_text("Say hello girl"))


# более короткая запись
# def is_hello_in_text(text):
#     return "hello" in text


# print(is_hello_in_text("Say hello girl"))


def greeting_depends_on_gender(name, gender):
    if gender == "male":
        print("Hello " + name + "! You like greate")
        return gender
    elif gender == "female":
        print("Hello " + name + "! You are so beautiful")
        return gender
    else:
        print("Hello " + name + "! I am not sure about your gender beast")
        return gender


# greeting_depends_on_gender("Jack", "male")
# greeting_depends_on_gender("Jane", "female")
# greeting_depends_on_gender("Ja", "ddmale")

returned_value1 = greeting_depends_on_gender("Jack", "male")
returned_value2 = greeting_depends_on_gender("Jane", "female")
returned_value3 = greeting_depends_on_gender("Ja", "ddmale")


# KWARGS and ARGS=====================================================================================


# def ten_percent_of_product(x, y):
#     return x * y * 0.1


# print(ten_percent_of_product(10, 20))


def ten_percent_of_product_with_args(*args):
    product = 1
    for num in args:
        product = product * num
    return product * 0.1


print(ten_percent_of_product_with_args(10, 30, 7, 2))


def percent_of_product_with_args(percent, *args):
    product = 1
    for num in args:
        product = product * num
    return product / 100 * percent


print(percent_of_product_with_args(10, 10, 30, 7, 2))

# kwargs example


def func_with_kargs(**kwargs):
    print(kwargs)


func_with_kargs(first=1, second=2, third=3)


def hello_with_kwargs(**kwargs):
    if "name" in kwargs:
        print("Hello " + kwargs["name"])
    else:
        print("I don't know your name")


hello_with_kwargs(gender="male", name="John")
hello_with_kwargs(gender="male")


def hello_with_grreting_and_kwargs(greeting, **kwargs):
    if "name" in kwargs:
        print("Hello " + greeting, kwargs["name"])
    else:
        print("I don't know your name")


hello_with_grreting_and_kwargs("ASSHOLE", gender="male", name="John")
# hello_with_grreting_and_kwargs(gender = 'male')


def func_with_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


# получаем tupple and dictionary
func_with_args_kwargs(1, 2, 3, name="John", age=30)
