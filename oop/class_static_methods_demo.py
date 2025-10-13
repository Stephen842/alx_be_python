class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: does not access class or instance data.
        Just performs a calculation.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: has access to the class itself (cls).
        Can use class attributes or modify them.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
