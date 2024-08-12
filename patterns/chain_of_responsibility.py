# chain_of_responsibility.py

from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ConcreteHandlerA(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == "A":
            return f"HandlerA: I'll handle {request}"
        else:
            return super().handle(request)

class ConcreteHandlerB(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        if request == "B":
            return f"HandlerB: I'll handle {request}"
        else:
            return super().handle(request)
