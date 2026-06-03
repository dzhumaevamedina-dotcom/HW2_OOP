class Ingredient:
    def __init__(self, name, quantity, unit):
        self._name = name
        self.quantity = quantity  # через сеттер
        self._unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        float_value = float(value)
        if float_value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float_value

    def __str__(self):
        return f"{self._name}: {self.quantity} {self._unit}"

    def __repr__(self):
        return f"Ingredient('{self._name}', {self.quantity}, '{self._unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self._name == other._name and self._unit == other._unit