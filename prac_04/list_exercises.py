# 1

# numbers = []
# for i in range(5):
#     input_number = int(input("Number:"))
#     numbers.append(input_number)
#
# print("The First Number is", numbers[0])
# print("The Last Number is", numbers[-1])
# print("The Smallest Number is", min(numbers))
# print("The Largest number is", max(numbers))
# print("The average of the numbers is", sum(numbers) / len(numbers))

#2

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Username:").lower()

while user_input not in usernames:
    print("Access Denied")
    user_input = input("Username:").lower()
print("Access Granted!")
