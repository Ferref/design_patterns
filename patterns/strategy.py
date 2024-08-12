from abc import ABC, abstractmethod

# Abstract Strategy class defines the interface for concrete strategies
class Strategy(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        # Abstract method to be implemented by all concrete strategies
        pass

# Concrete Strategy A implements the Strategy interface
class ConcreteStrategyA(Strategy):
    def execute(self, data: str) -> str:
        # Implementation of the execute method for Strategy A
        return f"Strategy A processed {data}"

# Concrete Strategy B implements the Strategy interface
class ConcreteStrategyB(Strategy):
    def execute(self, data: str) -> str:
        # Implementation of the execute method for Strategy B
        return f"Strategy B processed {data}"

# Context class uses a Strategy to execute an operation
class Context:
    def __init__(self, strategy: Strategy):
        # Initializes the context with a specific strategy
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        # Allows changing the strategy at runtime
        self._strategy = strategy

    def do_something(self, data: str):
        # Delegates the execution to the current strategy
        return self._strategy.execute(data)

# Client code example to demonstrate the Strategy pattern
if __name__ == '__main__':
    # Create ConcreteStrategy A and pass it to the Context
    context = Context(ConcreteStrategyA())
    result = context.do_something("some data")
    print(result)  # Outputs: Strategy A processed some data

    # Change the strategy to ConcreteStrategy B at runtime
    context.set_strategy(ConcreteStrategyB())
    result = context.do_something("some different data")
    print(result)  # Outputs: Strategy B processed some different data