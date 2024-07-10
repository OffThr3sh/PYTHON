todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            print("Enter the todo number for which you want to edit from below: ")
            for item in todos:
                print(item)
            number = int(input())
            number = number - 1
            print(f"Enter the todo that you want to replace with - \"{todos[number]}\"")
            new_todo = input()
            todos[number] = new_todo.strip()
            print("Removed Successfully !! Your New Todos are: ")
            for item in todos:
                print(item)
        case "exit":
            break

print("Bye!!")