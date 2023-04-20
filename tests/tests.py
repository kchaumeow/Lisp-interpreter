import io

from lisp_builtins import BUILTIN_ENV, BUILTIN_MACRO
from lisp_interpreter import Interpreter

interpreter = None


def setup_function():
    global interpreter
    interpreter = Interpreter(BUILTIN_ENV, BUILTIN_MACRO)


def read_code(filename):
    with io.open(filename) as f:
        code = ''.join(filter(lambda s: s.strip()[0] != "#", f.readlines()))
    return code


def test_while_loop():
    lisp_code = '''
    (begin
        (define counter 0)
        (while
            (< counter n)
            (begin
                (define counter (+ counter 1))
                (define x (* x 2))
            )
        )
        x
    )
    '''

    assert interpreter.run_code(lisp_code, x=2, n=2) == 8
    assert interpreter.run_code(lisp_code, x=10, n=3) == 80
    assert interpreter.run_code(lisp_code, x=20, n=4) == 320


def test_factorial_while():
    lisp_code = read_code("../factorial_while.lisp")
    assert interpreter.run_code(lisp_code, x=1) == 1
    assert interpreter.run_code(lisp_code, x=3) == 6
    assert interpreter.run_code(lisp_code, x=5) == 120


def test_factorial_rec():
    lisp_code = read_code("../factorial_rec.lisp")
    assert interpreter.run_code(lisp_code, x=1) == 1
    assert interpreter.run_code(lisp_code, x=3) == 6
    assert interpreter.run_code(lisp_code, x=5) == 120
