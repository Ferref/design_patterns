class Target:
    # Target interface expected by the client
    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    # Adaptee class with a different interface
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    # Adapter class to convert Adaptee's interface to Target's interface
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        # Adapt the specific request to the expected interface
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


if __name__ == "__main__":
    # Client code using the Target interface
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(adapter.request())  # Output: Adapter: (TRANSLATED) Special behavior of the Adaptee.
