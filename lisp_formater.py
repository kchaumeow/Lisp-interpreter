from lisp_interpreter import *


def format(ast: Executable):
    if isinstance(ast, Atom):
        print(ast, end='')
    elif isinstance(ast, List):
        print()
        print('(', end='')
        for item in ast.get_children():
            format(item)
            print(' ')
        print(')', end='')
