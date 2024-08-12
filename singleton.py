class Singleton:
    # Class attribute to hold the single instance of the class
    _instance = None

    def __new__(cls, value):
        # `__new__` is responsible for creating a new instance of the class
        if cls._instance is None:
            # If no instance exists, create a new one
            cls._instance = super().__new__(cls)
            # Initialize the value of the instance
            cls._instance.value = value
        # Return the single instance (whether newly created or existing)
        return cls._instance

    def __init__(self, value):
        # `__init__` is called to initialize the instance after it has been created
        # Prevent modification of the value if the instance already exists
        if not hasattr(self, 'value'):
            # Set the value only if it's not already set
            self.value = value

if __name__ == '__main__':
    # When this script is run directly, the following code will execute

    # Create the first instance of Singleton with value 10
    s1 = Singleton(10)
    # Attempt to create another instance of Singleton with value 20
    s2 = Singleton(20)

    # Print the value of the first instance
    print(s1.value)  # Output should be 10
    # Print the value of the second instance (which should be the same as the first)
    print(s2.value)  # Output should be 10
    # Check if both s1 and s2 are actually the same instance
    print(s1 is s2)  # Output should be True
