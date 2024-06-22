# Write a program to check whether a string is a palindrome or a symmetrical list

user_inp = input("Type your string here : ")
patternContainer = []


for charPicker in range (user_inp.__len__()//2 + 1) :
    patternContainer.append(user_inp[:charPicker])


def check_if_the_String_is_symmetrical():
    for pattern in patternContainer:
        if user_inp.count(pattern) == 2:
            return True
    return False


if check_if_the_String_is_symmetrical() :
    print("The string IS symmetrical")
else:
    print("The string is NOT symmetrical")


if user_inp == user_inp.__reversed__():
    print("The string IS a palindrome")
else:
    print("The string is NOT a palindrome")