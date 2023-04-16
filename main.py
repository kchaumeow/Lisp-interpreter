import io
from lisp_builtins import *
from lisp_interpreter import Interpreter
import sys

if __name__ == "__main__":

    arguments = sys.argv
    filename = arguments[1]
    should_format = "-f" in arguments

    interpreter = Interpreter(BUILTIN_ENV, BUILTIN_MACRO)

    with io.open(filename) as f:
        code = ''.join(filter(lambda s: s.strip()[0] != "#", f.readlines()))
        tokens = interpreter.tokenize(code)
        ast = interpreter.build_ast(tokens)

    if should_format:
        with io.open(filename, 'w') as f:
            f.write(ast.format_programm())
    else:
        print(interpreter.execute_ast(ast))
