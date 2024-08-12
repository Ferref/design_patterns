# Mediator interface
class Mediator:
    def notify(self, sender: str, event: str):
        raise NotImplementedError

# Concrete Mediator class
class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.set_mediator(self)
        self._component2 = component2
        self._component2.set_mediator(self)

    def notify(self, sender: str, event: str):
        if event == "A":
            print("Mediator reacts on A and triggers the following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers the following operations:")
            self._component1.do_b()

# Base Component class
class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

# Component1 class
class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self._mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")

# Component2 class
class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self._mediator.notify(self, "D")

# Client code
if __name__ == "__main__":
    component1 = Component1()
    component2
