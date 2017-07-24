from functools import wraps

def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person:
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print(my_person.get_fullname())

def tags(tags_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(*agrs,**kwargs):
            return "<{0}>{1}<{0}>".format(tags_name,func(*agrs,**kwargs))
        return func_wrapper
    return tags_decorator

@tags("p")
def get_text(name):
    """return some texts"""
    return name

# print(get_text("name"))
# print(get_text.__name__)
# print(get_text.__doc__) # returns some text
# print(get_text.__module__) # __main__