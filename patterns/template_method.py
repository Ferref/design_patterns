from abc import ABC, abstractmethod

# Abstract class defines the template method and the overall algorithm
class AbstractClass(ABC):
    def template_method(self) -> None:
        # This template method defines the skeleton of an algorithm
        self.base_operation()          # Base operation executed
        self.required_operations()     # Abstract method, to be implemented by subclasses
        self.hook()                    # Optional hook method that can be overridden

    def base_operation(self) -> None:
        # A base operation that is shared by all subclasses
        print("AbstractClass: Doing base operation.")

    @abstractmethod
    def required_operations(self) -> None:
        # An abstract method that must be implemented by concrete subclasses
        pass

    def hook(self) -> None:
        # A default hook method that can be overridden. It's optional behavior.
        pass

# Concrete implementation of the abstract class
class ConcreteClass1(AbstractClass):
    def required_operations(self) -> None:
        # Implements the required operation specific to ConcreteClass1
        print("ConcreteClass1: Implemented Operation1")

# Another concrete implementation of the abstract class
class ConcreteClass2(AbstractClass):
    def required_operations(self) -> None:
        # Implements the required operation specific to ConcreteClass2
        print("ConcreteClass2: Implemented Operation2")
    
    def hook(self) -> None:
        # Overrides the default hook method with specific behavior for ConcreteClass2
        print("ConcreteClass2: Overridden Hook")

# Client code example demonstrating the Template Method pattern
if __name__ == '__main__':
    # Create an instance of ConcreteClass1 and call the template method
    concrete1 = ConcreteClass1()
    concrete1.template_method()
    # Output:
    # AbstractClass: Doing base operation.
    # ConcreteClass1: Implemented Operation1

    print()  # Line break for clarity

    # Create an instance of ConcreteClass2 and call the template method
    concrete2 = ConcreteClass2()
    concrete2.template_method()
    # Output:
    # AbstractClass: Doing base operation.
    # ConcreteClass2: Implemented Operation2
    # ConcreteClass2: Overridden Hook