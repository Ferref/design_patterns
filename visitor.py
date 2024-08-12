from abc import ABC, abstractmethod

# Visitor interface declares a visiting method for each Concrete Element type.
class Visitor(ABC):
    @abstractmethod
    def visit(self, element: 'ConcreteElementA'):
        pass

    @abstractmethod
    def visit(self, element: 'ConcreteElementB'):
        pass

# Concrete Visitor implements the Visitor interface.
class ConcreteVisitor(Visitor):
    def visit(self, element: 'ConcreteElementA'):
        # Implementation for ConcreteElementA
        print(f"Visitor processing ConcreteElementA: {element.operation_a()}")

    def visit(self, element: 'ConcreteElementB'):
        # Implementation for ConcreteElementB
        print(f"Visitor processing ConcreteElementB: {element.operation_b()}")

# Element interface declares an accept method
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

# Concrete Element A
class ConcreteElementA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit(self)  # Accepts the visitor

    def operation_a(self) -> str:
        return "Operation in ConcreteElementA"

# Concrete Element B
class ConcreteElementB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit(self)  # Accepts the visitor

    def operation_b(self) -> str:
        return "Operation in ConcreteElementB"

# Object Structure class that contains elements
class ObjectStructure:
    def __init__(self):
        self._elements = []

    def add_element(self, element: Element):
        self._elements.append(element)

    def accept(self, visitor: Visitor):
        for element in self._elements:
            element.accept(visitor)  # Delegate to each element

# Client code demonstrating the Visitor pattern
if __name__ == '__main__':
    # Create an object structure and add elements to it.
    structure = ObjectStructure()
    structure.add_element(ConcreteElementA())
    structure.add_element(ConcreteElementB())

    # Create a visitor
    visitor = ConcreteVisitor()

    # Traverse the object structure and apply the visitor
    structure.accept(visitor)