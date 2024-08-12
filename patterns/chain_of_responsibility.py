# chain_of_responsibility.py

from abc import ABC, abstractmethod  # Importing the necessary modules for abstract base classes and abstract methods
from typing import Optional  # Importing Optional for type hinting optional return values

# The Handler interface declares methods for building the chain of handlers and for handling requests.
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: 'Handler') -> 'Handler':
        # This method is used to set the next handler in the chain.
        # It returns a handler, allowing the chaining of handlers in a convenient way.
        pass

    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        # This method handles the request. It should be implemented by concrete handlers.
        # If the handler can't handle the request, it should pass the request to the next handler in the chain.
        pass

# The default chaining behavior can be implemented inside a base handler class.
class AbstractHandler(Handler):
    _next_handler: Handler = None  # Initializing the next handler as None

    def set_next(self, handler: Handler) -> Handler:
        # Assigns the next handler in the chain.
        # Returns the handler that was passed, allowing chaining.
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> Optional[str]:
        # Handles the request. If this handler can't handle it, it passes the request to the next handler.
        if self._next_handler:
            return self._next_handler.handle(request)
        return None  # If no handler in the chain can handle the request, returns None

# Concrete Handlers either handle the request or pass it to the next handler in the chain.
class ConcreteHandlerA(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        # This handler handles the request if it's equal to "A".
        # Otherwise, it passes the request to the next handler.
        if request == "A":
            return f"HandlerA: I'll handle {request}"
        else:
            return super().handle(request)

class ConcreteHandlerB(AbstractHandler):
    def handle(self, request: str) -> Optional[str]:
        # This handler handles the request if it's equal to "B".
        # Otherwise, it passes the request to the next handler.
        if request == "B":
            return f"HandlerB: I'll handle {request}"
        else:
            return super().handle(request)
