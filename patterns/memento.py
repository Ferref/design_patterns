# Memento class that stores the state of the originator
class Memento:
    def __init__(self, state: str):
        # Initializes the memento with a specific state
        self._state = state

    def get_state(self) -> str:
        # Returns the stored state of the memento
        return self._state

# Originator class that creates and restores its state from a memento
class Originator:
    _state = None  # Holds the current state of the originator

    def set_state(self, state: str):
        # Sets the state of the originator and prints a message
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save(self) -> Memento:
        # Creates a memento containing the current state and returns it
        return Memento(self._state)

    def restore(self, memento: Memento):
        # Restores the state of the originator from the provided memento
        self._state = memento.get_state()
        print(f"Originator: State restored to {self._state}")

# Caretaker class that manages the mementos for the originator
class Caretaker:
    def __init__(self):
        # Initializes the caretaker with an empty list of mementos
        self._mementos = []
        self._originator = Originator()  # Creates an instance of the originator

    def backup(self):
        # Saves the current state of the originator by creating a memento
        self._mementos.append(self._originator.save())

    def undo(self):
        # Restores the most recent state of the originator from the memento
        if not self._mementos:
            return  # If there are no mementos, there's nothing to undo
        memento = self._mementos.pop()  # Get the last saved memento
        self._originator.restore(memento)  # Restore the originator's state