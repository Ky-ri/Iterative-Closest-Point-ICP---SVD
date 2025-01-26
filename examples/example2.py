#Directory fix
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import time
from src.utils import pointParser, plotCloud, plotClouds
from src.registration import IterativeClosestPoint

def main():
    fixed = pointParser("pointClouds\point_cloud_a.txt")
    moving = pointParser("pointClouds\point_cloud_b.txt")
    thres = 0.001
    maxIter = 100
    icp = IterativeClosestPoint(thres, maxIter)
    
    print('Starting... ')
    start = time.time()

    _,errStorage,_ = icp.register(fixed, moving)
    
    fin = time.time()
    print('\nDONE...')
    print('Total Time: {} s'.format(fin-start))

if __name__ == "__main__":
    main()          