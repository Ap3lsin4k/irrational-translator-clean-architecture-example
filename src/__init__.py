#__init__.py
from presentation.ua_lang_controller import Controller

class A:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value%3

if __name__ == '__main__':
    b = A()
    b.i = 10
    print(b.i)
