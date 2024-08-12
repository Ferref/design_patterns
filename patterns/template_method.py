from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation()
        self.required_operations()
        self.hook()

    def base_operation(self) -> None:
        print("AbstractClass: Doing base operation.")

    @abstractmethod
    def required_operations(self) -> None:
        pass

    def hook(self) -> None:
        pass

class ConcreteClass1(AbstractClass):
    def required_operations(self) -> None:
        print("ConcreteClass1: Implemented Operation1")

class ConcreteClass2(AbstractClass):
    def required_operations(self) -> None:
        print("ConcreteClass2: Implemented Operation2")
    
    def hook(self) -> None:
        print("ConcreteClass2: Overridden Hook")
