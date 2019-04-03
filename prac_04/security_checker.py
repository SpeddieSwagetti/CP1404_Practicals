usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

user_input = input()

if user_input not in usernames:
    print("Access denied")
for i in range(0, len(usernames), 1):
    if user_input == usernames[i]:
        print("Access granted")
        break
    else:
        continue
