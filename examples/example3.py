#Directory fix
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import numpy as np
import time
from src.oper import R_x, R_y, R_z
from src.utils import pointParser, plotCloud, plotClouds
from src.registration import IterativeClosestPoint

def main():
    # import a point cloud
    fixed = pointParser("pointClouds\point_cloud_a.txt")
    thres = 0.001
    maxIter = 100
    #plotCloud(fixed, "Fixed Cloud") #Initial cloud plot

    # define a translation and rotation for the points
    translation = np.array([1.0, 0.0, 0.0])
    rotation = R_z(45)
    #rotation = R_z(45) @ R_x(45)
    
    moving = (rotation.dot(fixed.T)).T # apply the roto-translation
    moving = np.add(moving, translation)

    plotClouds(fixed, moving, -1, False)
    icp = IterativeClosestPoint(thres, maxIter, plotOrNot=False, savePlots=True)
    
    print('Starting... ')
    start = time.time()

    _,errStorage, new_moving = icp.register(fixed, moving)
    
    fin = time.time()
    print('\nDONE...')
    print('Total Time: {} s'.format(fin-start))
    plotClouds(fixed, new_moving, -1, False)


if __name__ == "__main__":
    main()          