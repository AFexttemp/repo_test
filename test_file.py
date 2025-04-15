import sys
import os
import time




time.sleep(2)

class MyClass:
    def __init__(self) -> None:
        pass

    def my_print(self) -> None:
        print("is OK")

def test_function() -> None:
    print(os.getcwd())
    print(sys.stdout)
    print("in test function")