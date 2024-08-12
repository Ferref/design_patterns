class Product:
    # A complex object to be constructed by the builder
    def __init__(self):
        # Initialize product components
        self.parts = []

    def add(self, part):
        # Add a part to the product
        self.parts.append(part)

    def show(self):
        # Display the product parts
        print("Product parts: ", self.parts)


class Builder:
    # Abstract builder interface
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        # Abstract method to build part A
        pass

    def build_part_b(self):
        # Abstract method to build part B
        pass

    def get_product(self):
        # Return the constructed product
        return self.product


class ConcreteBuilder(Builder):
    # Concrete implementation of the builder
    def build_part_a(self):
        # Implement building of part A
        self.product.add("Part A")

    def build_part_b(self):
        # Implement building of part B
        self.product.add("Part B")


class Director:
    # Director class that constructs a product using the builder
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        # Construct the product using the builder
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    # Create a builder instance
    builder = ConcreteBuilder()
    # Create a director with the builder
    director = Director(builder)
    # Construct the product
    director.construct()
    # Retrieve the final product
    product = builder.get_product()
    # Show the product
    product.show()  # Output should be: Product parts: ['Part A', 'Part B']
