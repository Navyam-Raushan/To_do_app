# First take command from user
# todos = [] no need to create a list its done by readlines method.
import functions
import time

# To show current time and date. 
now = time.strftime("%b %d %H:%M:%S")

print("Welcome, Its", now)
while True:

    userAction = input("Type add, show, complete, edit or exit: ")
    userAction = userAction.lower().strip()
    # Using match case for all given commands.

    if userAction.startswith("add"):
        newTodo = userAction[4:]
        # This is a line to read it back help to store all todos.
        # file = open("Files/todos.txt", "r")
        # # store it into todos variable to iterate it.
        # todos = file.readlines()
        # file.close()
        # Using with context manager to do the same thing

        todos = functions.read_todos()

        todos.append(newTodo + "\n")

        # file = open("Files/todos.txt", "w")
        # file.writelines(todos)
        # file.close()

        functions.write_todos(todos)

    elif userAction.startswith("show"):
        # we have to open todos here to show it
        # file = open("Files/todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        # todos = [t.title().strip() for t in todos]  # use of list comprehension
        todos = functions.read_todos()

        for index, t in enumerate(todos):
            t = t.title().strip()
            # print(index,t)

            # using f strings to print variables same as $ in js
            toPrint = f"{index + 1}- {t}"
            print(toPrint)

    elif userAction.startswith("edit"):
        try:

            # In this by entering index we are editing but user counts from 1..
            index = int(userAction[5:])
            todos = functions.read_todos()

            todos[index - 1] = input("Enter edited todo: ") + "\n"

            # This part is writing the edited todos so first edit then write.
            # file = open("Files/todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            functions.write_todos(todos)

        except ValueError:
            print("Please enter number of particular todo")
            continue
        except IndexError:
            print("There is no todo at that number")
            continue

    # This case is for completed todos, removing it from the list.
    elif userAction.startswith("complete"):
        try:
            index = int(userAction[9:])
            index = index - 1

            todos = functions.read_todos()

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            # This part is re writing the todos which is available.
            # file = open("Files/todos.txt", "w")
            # file.writelines(todos)
            # file.close()

            functions.write_todos(todos)

            # its good to display a message which todo is removed.
            message = f"Todo '{todo_to_remove}' is removed from list."
            print(message.title())
        except IndexError:
            print("There is no todo at that number")
            continue
        except ValueError:
            print("Please enter number of particular todo")
            continue

    elif userAction.startswith("exit"):
        break

    # This case is executed if no any case matches.
    else:
        print("Command is not valid..")
