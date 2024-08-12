# Define the state interface that will be implemented by concrete states.
class State:
    def handle(self, context):
        raise NotImplementedError("Handle method must be overridden.")

# Define a concrete state that implements the handle method.
class ConcreteStateA(State):
    def handle(self, context):
        print("State A is handling the request.")
        context.state = ConcreteStateB()  # Change the state of the context.

# Define another concrete state that implements the handle method.
class ConcreteStateB(State):
    def handle(self, context):
        print("State B is handling the request.")
        context.state = ConcreteStateA()  # Change the state of the context.

# Define the context that maintains an instance of a concrete state.
class Context:
    def __init__(self, state: State):
        self.state = state  # The current state of the context.

    def request(self):
        self.state.handle(self)  # Delegate the request to the current state.

# Client code
if __name__ == "__main__":
    # Initialize the context with an initial state.
    context = Context(ConcreteStateA())

    # Request method will change the state each time it is called.
    context.request()  # State A will handle this and change to State B.
    context.request()  # State B will handle this and change to State A.
    context.request()  # State A will handle this and change to State B.
