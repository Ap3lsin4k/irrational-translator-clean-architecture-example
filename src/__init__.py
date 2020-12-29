#__init__.py
import builtins

from os import open
if __name__ == '__main__':
    v = builtins
    v.print("something")
    f = open(r"fіlе.tхt", "w")
    f.write("мій\nрядок\ny\nфайлі")
    f.close()
    f = open(r"fіlе.tхt", "r")
    print(f.__next__())
    f.close()