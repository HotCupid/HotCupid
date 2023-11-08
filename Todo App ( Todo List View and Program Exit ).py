todos = []

while True:
    user_action = input("Type 'add' to add a todo, 'show' to show your todos or 'exit' to exit the programme: \n")

    match user_action:
        case 'add':
            todo = input("Enter a TODO: ")
            todos.append(todo)

        case 'show':
            print(todos)

        case 'exit':
            break
print("Be sure to check in on your TODO list once a while")








