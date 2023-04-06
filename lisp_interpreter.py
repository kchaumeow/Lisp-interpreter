from __future__ import annotations


class Executable:
    def execute(self, interpreter):
        raise NotImplementedError()


class Atom(Executable):
    def __init__(self, value: str):
        self.__value = value

    def execute(self, interpreter):
        if self.__value.isnumeric():
            return int(self.__value)
        elif self.__value in interpreter.env:
            return interpreter.env[self.__value]
        return self.__value

    def format(self, indent_level=0):
        return "\t" * indent_level + self.__value
    @property
    def value(self):
        return self.__value

    def __str__(self):
        return self.__value


class List(Executable):
    def __init__(self, children: list[any]):
        self.__children = children
    def get_children(self):
        return self.__children
    def get_head(self):
        if len(self.__children) > 0:
            return self.__children[0]
        return None

    def get_tail(self):
        if len(self.__children) > 1:
            return self.__children[1:]
        return []

    def execute(self, interpreter):
        head, tail = self.get_head(), self.get_tail()
        if head is None:
            return None
        fn = interpreter.execute_ast(head)
        if fn in interpreter.macro:
            return interpreter.macro[fn](interpreter, *tail)
        elif callable(fn):
            return fn(interpreter.env, *[interpreter.execute_ast(i) for i in tail])
        return fn

    def format(self, indent_level=0):
        result = "\t" * indent_level + '('+self.get_head().value
        for child in self.__children[1:]:
            if isinstance(child, Atom):
                result +=  " " + child.value
            else: result += '\n' + child.format(indent_level + 1)
        if not isinstance(self.__children[-1], Atom):
            result += '\n' + "\t" * indent_level
        result += ')'
        return result
    @property
    def children(self):
        return self.__children

    def __str__(self):
        return f"({' '.join([str(i) for i in self.__children])})"


class Interpreter:
    def __init__(self, env=None, macro=None):
        self.env = {} if env is None else env.copy()
        self.macro = {} if macro is None else macro.copy()

    @staticmethod
    def tokenize(code: str) -> list[str]:
        return code.replace('(', ' ( ').replace(')', ' ) ').split()

    @staticmethod
    def build_ast(tokens: list[str]) -> Executable:
        safe = []
        while len(tokens):
            token = tokens.pop(0)
            if token == '(':
                safe.append(Interpreter.build_ast(tokens))
            elif token == ')':
                return List(safe)
            else:
                safe.append(Atom(token))
        return safe[0]

    def execute_ast(self, ast: Executable, *, env=None):
        if env is not None:
            return Interpreter(env, self.macro).execute_ast(ast)
        return ast.execute(self)
