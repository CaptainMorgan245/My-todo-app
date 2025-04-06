FILEPATH = "todos.txt"  #FILEPATH = "todos.txt"  #FILEPATH = "../todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

    # function return none and is just a procedure


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write tghe to-do item to a text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def show_list():
    todos = get_todos()

    for index, item in enumerate(todos):
        item = item.title()
        item = item.strip('\n')
        row = f"{index + 1}: {item}"
        print(row)


