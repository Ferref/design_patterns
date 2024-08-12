from abc import ABC, abstractmethod  # Importing necessary modules for defining abstract base classes and methods

# The Command interface declares a method for executing a command.
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        # This abstract method should be implemented by concrete command classes.
        # It will contain the action to be executed.
        pass

# The Receiver class contains the business logic and operations that are triggered by the command.
class Receiver:
    def operation(self, data: str):
        # This method simulates some operation performed by the receiver.
        # It takes a string 'data' as input and prints a message indicating work being done.
        print(f"Receiver: Working on {data}")

# ConcreteCommand implements the Command interface and links the receiver to an action.
class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver, data: str):
        # Initializes the command with a receiver and the data needed for the operation.
        self._receiver = receiver
        self._data = data

    def execute(self) -> None:
        # When the command is executed, it calls the receiver's operation method with the provided data.
        self._receiver.operation(self._data)

# The Invoker is responsible for storing and executing commands.
class Invoker:
    def __init__(self):
        # Initializes an empty list to store commands.
        self._commands = []

    def add_command(self, command: Command):
        # Adds a command to the list of commands to be executed.
        self._commands.append(command)

    def execute_commands(self):
        # Iterates over the list of commands and executes each one.
        for command in self._commands:
            command.execute()
