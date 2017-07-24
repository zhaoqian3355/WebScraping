from functools import wraps

def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message

greet=compose_greet_func("John")

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))

    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))

    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def simple_decorator(function):
    print("doing decoration")
    return function

def decorator_with_arguments(arg):
    print("defining the decorator")
    def _decorator():
        print("doing decoration, %r"%arg)
        return arg

    return _decorator

# print(get_text("John"))

class Person:
    def __init__(self):
        self.name="John"
        self.family="Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person=Person()

# print(my_person.get_fullname())

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    return "Hello "+name

# print(get_text("John"))
# print(get_text.__name__)

@decorator_with_arguments
def function():
    print("inside function")

function()