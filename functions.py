FILE_PATH = "todos.txt"


def read_todos(file_path=FILE_PATH):
    """ Read text file and return a list of items. """
    with open(file_path, 'r') as read_file_local:
        todos_local = read_file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILE_PATH):
    """ Write items in text file. """
    with open(file_path, 'w') as write_file_local:
        write_file_local.writelines(todos_arg)


if __name__ == '__main__':
    print("hello mahmoud taha")

