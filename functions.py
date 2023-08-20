# Using function to avoid reduntancy (code repeatn)
# if we mention anything inside parameter its a default argument for that function.
# Storing it into another file for better codebase.

FILEPATH = "todos.txt"


def read_todos(filepath=FILEPATH):
    """ Read a file which contain
    to-do items."""

    with open(filepath, "r") as local_file:
        local_todos = local_file.readlines()
        return local_todos


def write_todos(local_todos, filepath=FILEPATH):
    """Write the to-do items in the file."""

    with open(filepath, "w") as local_file:
        local_file.writelines(local_todos)
