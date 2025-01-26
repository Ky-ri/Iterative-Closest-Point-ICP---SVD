import numpy as np

# Rotation on the X-axis.
def R_x(degrees):

    theta = np.radians(degrees)
    return np.array([[1, 0, 0],
                      [0, np.cos(theta), -np.sin(theta)],
                      [0, np.sin(theta), np.cos(theta)]])

# Rotation on the Y-axis.
def R_y(degrees):

    theta = np.radians(degrees)
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                      [0, 1, 0],
                      [-np.sin(theta), 0, np.cos(theta)]])

# Rotation on the Z-axis.
def R_z(degrees):
    
    theta = np.radians(degrees)
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta), np.cos(theta), 0],
                      [0, 0, 1]])


