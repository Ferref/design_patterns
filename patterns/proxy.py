from abc import ABC, abstractmethod

# Abstract Subject class that defines the interface for the RealSubject and Proxy classes
class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        # Abstract method to be implemented by all concrete subjects
        pass

# RealSubject class implements the Subject interface providing actual functionality
class RealSubject(Subject):
    def request(self) -> None:
        # Implementation of the request handling in the RealSubject
        print("RealSubject: Handling request.")

# Proxy class that controls access to the RealSubject
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        # Initializes the Proxy with an instance of RealSubject
        self._real_subject = real_subject

    def request(self) -> None:
        # The Proxy can perform additional tasks before delegating to the RealSubject
        if self.check_access():  # Check if access is allowed
            self._real_subject.request()  # Delegate the request to the RealSubject
            self.log_access()  # Log the request after it has been processed

    def check_access(self) -> bool:
        # Simulates an access control check
        print("Proxy: Checking access.")
        return True  # For this example, access is always allowed

    def log_access(self) -> None:
        # Logs the request for auditing or other purposes
        print("Proxy: Logging the request.")

# Client code example to demonstrate Proxy behavior
if __name__ == '__main__':
    # Creating an instance of the RealSubject
    real_subject = RealSubject()
    
    # Creating a Proxy that encapsulates the RealSubject
    proxy = Proxy(real_subject)
    
    # Client makes a request via the Proxy
    proxy.request()  # This will check access, log, and then delegate to the RealSubject