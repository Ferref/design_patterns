from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Receiver:
    def operation(self, data: str):
        print(f"Receiver: Working on {data}")

class ConcreteCommand(Command):
    def __init__(self, receiver: Receiver, data: str):
        self._receiver = receiver
        self._data = data

    def execute(self) -> None:
        self._receiver.operation(self._data)

class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()
