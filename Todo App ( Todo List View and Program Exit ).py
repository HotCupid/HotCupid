todos = []

while True:
    user_action = input("Type 'add' to add a todo, 'show' to show your todos or 'exit' to exit the programme: \n")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a TODO: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'exit':
            break
        case whatever:
            print("Please read the instructions carefully \n")
print("Be sure to check in on your TODO list once a while")








