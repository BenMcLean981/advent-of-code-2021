class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: "Vector") -> "Vector":
        # I prefer classes for encapsulation, but I like to write non-modifying
        # pure functions like this one, it doesn't change any of the inputs.
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
