import math
class Vector2D:
    def _init_(self, x, y):
        self.x = x 
        self.y = y 

    def magnitude(self):
        return math.sqrt(self.x*2 + self.y*2)

    def rotation(self):
        return math.atan2(self.y, self.x)

    def distance(self, other):
        return math.sqrt((self.x - other.x)*2 + (self.y - other.y)*2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def _init_(self, x, y, z):
        super()._init_(x, y) 
        self.z = z  

    def magnitude(self):
        return math.sqrt(self.x*2 + self.y*2 + self.z*2)

    def rotation(self):
        return math.atan2(self.y, self.x)

    def distance(self, other):
        return math.sqrt((self.x - other.x)*2 + (self.y - other.y)*2 + (self.z - other.z)*2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

def user_input():
    print("Choose the type of vector:")
    print("1. 2D Vector")
    print("2. 3D Vector")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        x = float(input("Enter x-coordinate: "))
        y = float(input("Enter y-coordinate: "))
        vector1 = Vector2D(x, y)
        
        print(f"Vector Magnitude: {vector1.magnitude()}")
        print(f"Vector Rotation (radians): {vector1.rotation()}")

        x2 = float(input("Enter x-coordinate of another vector: "))
        y2 = float(input("Enter y-coordinate of another vector: "))
        vector2 = Vector2D(x2, y2)

        print(f"Distance between vectors: {vector1.distance(vector2)}")
        print(f"Dot product of vectors: {vector1.dot_product(vector2)}")
        print(f"Cross product of vectors: {vector1.cross_product(vector2)}")

    elif choice == '2':
        x = float(input("Enter x-coordinate: "))
        y = float(input("Enter y-coordinate: "))
        z = float(input("Enter z-coordinate: "))
        vector1 = Vector3D(x, y, z)
        
        print(f"Vector Magnitude: {vector1.magnitude()}")
        print(f"Vector Rotation (radians): {vector1.rotation()}")

        x2 = float(input("Enter x-coordinate of another vector: "))
        y2 = float(input("Enter y-coordinate of another vector: "))
        z2 = float(input("Enter z-coordinate of another vector: "))
        vector2 = Vector3D(x2, y2, z2)

        print(f"Distance between vectors: {vector1.distance(vector2)}")
        print(f"Dot product of vectors: {vector1.dot_product(vector2)}")

        cross_product = vector1.cross_product(vector2)
        print(f"Cross product of vectors: ({cross_product.x}, {cross_product.y}, {cross_product.z})")

    else:
        print("Invalid choice.")
user_input()