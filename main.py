import io

from lisp_builtins import BUILTIN_ENV, BUILTIN_MACRO
from lisp_interpreter import Interpreter

if __name__ == "__main__":
    interpreter = Interpreter(BUILTIN_ENV, BUILTIN_MACRO)
    with io.open('code.lisp') as f:
        code = ''.join(f.readlines())
        print(code)
        tokens = interpreter.tokenize(code)
        print(tokens)
        ast = interpreter.build_ast(tokens)
        print(ast)
        print(interpreter.execute_ast(ast))
