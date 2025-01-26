import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import sample

def samplePointCloud(cloud, percent):
    """Returns a subset of the point cloud. Speeds up the plotting.

    Args:
        cloud (_type_): Point of cloud to sample.
        percent (float): Percentage of the point cloud to sample.

    Returns:
        _type_: X, Y, Z coordinates of the sampled point cloud.
    """    
    l = cloud.shape[0]
    indices = sample(range(l), int(l * percent))
    x_sampled = np.array(cloud[0:,0])[indices]
    y_sampled = np.array(cloud[0:,1])[indices]
    z_sampled = np.array(cloud[0:,2])[indices]

    return x_sampled, y_sampled, z_sampled

def plotClouds(fixed, moving, iter, plot=False, save=False):
    """Plots the Fixed and Moving point Clouds.

    Args:
        fixed (_type_): Fixed point cloud.
        moving (_type_): Moving point cloud.
        iter (_type_): Iteration number.
        plot (bool): Plot option. Defaults to False.
        save (bool, optional): Save option. Defaults to False.
    """    
    sampled = True # Sample the point clouds to plot 

    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(111, projection='3d')

    if sampled:
        fixedSamples_x, fixedSamples_y, fixedSamples_z = samplePointCloud(fixed, 0.2)
        movingSamples_x, movingSamples_y, movingSamples_z = samplePointCloud(moving, 0.2)
        ax.plot_trisurf(fixedSamples_x, fixedSamples_y, fixedSamples_z, cmap='Greens', edgecolor='none')
        ax.plot_trisurf(movingSamples_x, movingSamples_y, movingSamples_z, cmap='Reds', edgecolor='none')
    
    else:
        ax.plot_trisurf(fixed[0:,0], fixed[0:,1], fixed[0:,2], cmap='Greens', edgecolor='none')
        ax.plot_trisurf(moving[0:,0], moving[0:,1], moving[0:,2], cmap='Reds', edgecolor='none')
    
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.zaxis.label.set_position((0.5, 1.05))

    title = '3D point clouds plot Iter = ' + str(iter) 
    ax.set_title(title)

    plt.tight_layout()
    if plot: plt.show()

    filename = 'plot_' + str(iter) + '.png'
    if save: fig.savefig(filename, dpi=300)
    plt.close(fig)

def plotCloud(cloud, title = ""):
    """Plots a 3D point Cloud.

    Args:
        cloud (_type_): Point cloud to plot.
        title (str, optional): Plot title. Defaults to "".
    """    
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(projection='3d')

    ax.plot_trisurf(cloud[0:,0], cloud[0:,1], cloud[0:,2], cmap='viridis', edgecolor='none')
    #ax.scatter(cloud[0:,0], cloud[0:,1], cloud[0:,2], c='r', marker='o') # FASTER!!!

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    title += "" 
    ax.set_title(title)

def errplotter(errStorage):
    """Plots the error conversion of the algorithm.

    Args:
        errStorage (_type_): Error evolution.
    """    
    plt.plot(errStorage)
    plt.ylabel('Error Convergence')
    plt.xlabel('Iterations')
    plt.show()

def pointParser(fileName):
    """Parses a file containing 3D points and converts the data into a NumPy array

    Args:
        fileName (string): File name of the point cloud.

    Returns:
        numpy array: Numpy array containing the 3D points.
    """    
    temp = []
    with open(fileName) as f:
            for l in f:
                    x, y, z = l.split()
                    temp.append([float(x), float(y), float(z)])
                    
    return np.asarray(temp)