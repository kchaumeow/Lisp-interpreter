import matplotlib.pyplot as plt
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
        return interpreter.execute_ast(body[1])


def builtin_while(interpreter: Interpreter, condition_expr, body):
    while interpreter.execute_ast(condition_expr):
        interpreter.execute_ast(body)


def draw_mandelbrot(e, mandelbrot):

    # Define the parameters of the Mandelbrot set

    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
    width, height = 300, 300

    # Create the Tkinter window and canvas
    window = tk.Tk()
    window.title("Mandelbrot fractal")
    canvas = tk.Canvas(window, width=width, height=height, bg="#FFFFFF")
    canvas.pack()

    # Draw the Mandelbrot set on the canvas
    for x in range(width):
        for y in range(height):
            c = complex(xmin + (xmax - xmin) * x / width, ymin + (ymax - ymin) * y / height)
            color = mandelbrot(e, c)
            canvas.create_line(x, y, x + 1, y + 1, fill=color)

    window.mainloop()


def draw_bifur(e, c, s):
    plt.plot(c, s, 'b.', ms=1)
    plt.show()


BUILTIN_ENV = {
    '+': lambda e, a, b: a + b,
    '-': lambda e, a, b: a - b,
    '*': lambda e, a, b: a * b,
    '/': lambda e, a, b: a // b,
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
    'print': lambda e, *a: print(*a),
    'prompt': lambda e: input(),
    'draw_mandelbrot': draw_mandelbrot,
    'abs': lambda e, a: abs(a),
    'pow': lambda e, *a: pow(*a),
    'len': lambda e, a: len(a),
    'max': lambda e, *a: max(a),
    'min': lambda e, *a: min(a),
    'call': lambda e, root, func_name, *a: getattr(root, func_name)(*a),
    'list': lambda e, *a: [*a],
    'draw_bifur': draw_bifur,
    'typeof': lambda e, a: type(a),
    'float': lambda e, a: float(a),
}

BUILTIN_MACRO = {
    'lambda': internal_lambda,
    'if': builtin_if,
    'while': builtin_while,
    'define': builtin_define,
}
