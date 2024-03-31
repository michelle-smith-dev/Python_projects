# inp = input("Provide a 3 digit number: ")
# list1 = list(inp)


def user_input():
    prompt = 'Type any digit, 3 characters or more: '
    while True:
        usr_inp = input(prompt)
        if usr_inp.isdigit():
            break
        else:
            print('invalid command')


def palindrome(number):
    list1 = list(number)
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1


def compare(val):
    # conv = ""
    # for i in range(len(val)):
    #     conv += val[i]
    conv = "".join(val)
    print(conv)
    print(user_input)
    if conv == user_input:
        print("Yes, this is a palindrome number.")
    else:
        print("No, this is not a palindrome number.")


palindrome(user_input())
# compare(v)

