from abc import ABC, abstractmethod

class absClass(ABC):
    def print(self,x):
        print("Value:",x)
    
    @abstractmethod
    def task(self):
        print("We are inside of absClass")

class test_class(absClass):
    def task(self):
        print("We are inside of test_class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)