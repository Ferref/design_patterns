from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, data: str) -> str:
        pass

class ConcreteStrategyA(Strategy):
    def execute(self, data: str) -> str:
        return f"Strategy A processed {data}"

class ConcreteStrategyB(Strategy):
    def execute(self, data: str) -> str:
        return f"Strategy B processed {data}"

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something(self, data: str):
        return self._strategy.execute(data)
