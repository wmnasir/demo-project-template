# item = "Banana"
# Item = "Apple"
# item_name = "Orange"
# print(item, Item)
# print("Hello " + item_name)

# integer = 2021
# word = "text"
# isHappy = False
# naughty_list = ["John", "Jane", "Jack"]
# print(integer)
# print(word)
# print(isHappy)
# print(naughty_list)

# integer = 2021
# name = "John"
# string_number = "21"
# print(integer + int(string_number))
# print(name + str(integer))

# a = 10
# b = 4
# addition = a + b
# difference = a - b
# divide = a / b
# power = a**b
# print(addition)
# print(difference)
# print(divide)
# print(power)

# age = 18
# isHappy = False
# if age > 21:
#     print("You are older than 21")
#     if isHappy:
#         print("You are happy")
#     else:
#         print("You are not happy")
# elif age == 21:
#     print("You are 21")
#     print("Reach here")
# else:
#     print("You are younger than 21")
#     print("Reach here")

# for i in range(3):
#     print("Hello", i)

# print(range(3))
# print(list(range(3)))
# print(list(range(1, 3)))


def get_discount(age):
    if age > 60:
        return 0.70  # 70% discount
    elif age < 2:
        return 0.50  # 50% discount
    else:
        return 0.00  # no discount


# Example usage:
print(get_discount(65))  # Output: 0.70
print(get_discount(1))  # Output: 0.50
print(get_discount(30))  # Output: 0.00
