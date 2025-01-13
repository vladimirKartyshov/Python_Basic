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
