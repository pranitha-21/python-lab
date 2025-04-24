import numpy as np

def cartesian_to_polar(points):
     
    x = points[:, 0]
    y = points[:, 1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return np.column_stack((r, theta))


N = 5  
cartesian_points = np.random.randint(-10, 10, size=(N, 2))
polar_points = cartesian_to_polar(cartesian_points)
print("Cartesian Coordinates:\n", cartesian_points)
print("\nPolar Coordinates (r, theta in radians):\n", polar_points)
