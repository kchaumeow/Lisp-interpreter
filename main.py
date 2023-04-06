import io
from lisp_formater import *
from lisp_builtins import BUILTIN_ENV, BUILTIN_MACRO
from lisp_interpreter import Interpreter

if __name__ == "__main__":
    def exec(filename):
        interpreter = Interpreter(BUILTIN_ENV, BUILTIN_MACRO)
        with io.open(filename) as f:
            code = ''.join(filter(lambda s: '#' not in s, f.readlines()))
            # print(code)
            tokens = interpreter.tokenize(code)
            print(tokens)
            ast = interpreter.build_ast(tokens)
            print(ast.format())
            print(interpreter.execute_ast(ast))
    exec('factorial_rec.lisp')
    exec('factorial_while.lisp')
    exec('Mandelbrot.lisp')
