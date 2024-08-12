class Component:
    # Base component interface
    def operation(self):
        pass


class ConcreteComponent(Component):
    # Concrete component implementation
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    # Base decorator class wrapping a component
    def __init__(self, component):
        self._component = component

    def operation(self):
        # Forward the operation to the wrapped component
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    # Concrete decorator A adds additional behavior
    def operation(self):
        return f"ConcreteDecoratorA({super().operation()})"


class ConcreteDecoratorB(Decorator):
    # Concrete decorator B adds additional behavior
    def operation(self):
        return f"ConcreteDecoratorB({super().operation()})"


if __name__ == "__main__":
    # Client code
    simple = ConcreteComponent()
    print(f"Simple: {simple.operation()}")  # Output: Simple: ConcreteComponent

    decorated_a = ConcreteDecoratorA(simple)
    decorated_b = ConcreteDecoratorB(decorated_a)
    print(f"Decorated: {decorated_b.operation()}")  # Output: Decorated: ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))
