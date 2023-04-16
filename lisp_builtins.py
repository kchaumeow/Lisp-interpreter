import math
import tkinter as tk
from lisp_interpreter import List, Atom, Interpreter


def builtin_define(interpreter: Interpreter, name, value):
    assert isinstance(name, Atom), "WHAT DID YOU WRITE EXACTLY? TRY AGAIN"
    interpreter.env[name.value] = interpreter.execute_ast(value)


def internal_lambda(interpreter: Interpreter, params, expr):
    if isinstance(params, List):
        params = [i.value for i in params.children]
    elif isinstance(params, Atom):
        params = [params.value]

    def func(env, *args):
        env = env.copy()
        env.update(zip(params, args))
        return interpreter.execute_ast(expr, env=env)

    return func


def builtin_if(interpreter: Interpreter, condition_expr, *body):
    condition = interpreter.execute_ast(condition_expr)
    if condition:
        return interpreter.execute_ast(body[0])
    elif len(body) > 1:
        print(body)
        return interpreter.execute_ast(body[1])


def builtin_while(interpreter: Interpreter, condition_expr, body):
    while interpreter.execute_ast(condition_expr):
        interpreter.execute_ast(body)


def draw(e):
    def mandelbrot(c):
        z = 0
        n = 0
        while abs(z) <= 2 and n < 255:
            z = z * z + c
            n += 1
        if n == 255:
            return "#FFFFFF"  # black if in the set
        else:
            return "#" + "{0:02x}{1:02x}{2:02x}".format(n, n, n)  # gray scale based on iteration count

    # Define the parameters of the Mandelbrot set

    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 500, 500

    # Create the Tkinter window and canvas
    window = tk.Tk()
    window.title("Mandelbrot fractal")
    canvas = tk.Canvas(window, width=width, height=height, bg="#FFFFFF")
    canvas.pack()

    # Draw the Mandelbrot set on the canvas
    for x in range(width):
        for y in range(height):
            c = complex(xmin + (xmax - xmin) * x / width, ymin + (ymax - ymin) * y / height)
            color = mandelbrot(c)
            canvas.create_line(x, y, x + 1, y + 1, fill=color)

    # Start the Tkinter event loop
    window.mainloop()
    # width, height = 500, 500
    #
    # # Create the Tkinter window and canvas
    # window = tk.Tk()
    # canvas = tk.Canvas(window, width=width, height=height, bg="#FFFFFF")
    # canvas.pack()
    # window.mainloop()


BUILTIN_ENV = {
    '+': lambda e, a, b: int(a) + int(b),
    '-': lambda e, a, b: int(a) - int(b),
    '*': lambda e, a, b: int(a) * int(b),
    '/': lambda e, a, b: int(a) // int(b),
    '>': lambda e, a, b: int(a) > int(b),
    '<': lambda e, a, b: int(a) < int(b),
    '>=': lambda e, a, b: int(a) >= int(b),
    '<=': lambda e, a, b: int(a) <= int(b),
    '==': lambda e, a, b: int(a) == int(b),
    '&&': lambda e, a, b: a and b,
    '||': lambda e, a, b: a or b,
    '!': lambda e, a: not a,
    'true': lambda e: True,
    'false': lambda e: False,
    'begin': lambda e, *a: a[-1],
    'print': lambda e, a: print(a),
    'prompt': lambda e: input(),
    'draw': draw,
    'abs': lambda e, a: abs(a),
    'pow': lambda e, *a: pow(*a),
    'len': lambda e, a: len(a),
    'max': lambda e, *a: max(a),
    'min': lambda e, *a: min(a),
    'call': lambda e, root, func_name, *a: getattr(root, func_name)(*a)
}

BUILTIN_MACRO = {
    'lambda': internal_lambda,
    'if': builtin_if,
    'while': builtin_while,
    'define': builtin_define
}
