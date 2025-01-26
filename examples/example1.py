#Directory fix
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import numpy as np
import argparse
import time
from src.utils import pointParser, plotCloud, plotClouds, errplotter
from src.registration import IterativeClosestPoint

def cmdparser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--fix", type = str, default = 'pointClouds\point_cloud_a.txt',
                        help = " filename of fixed point point cloud")
    parser.add_argument("--mov", type = str, default = 'pointClouds\point_cloud_b.txt',
                        help = " filename of moving point point cloud")
    parser.add_argument("--thres", type = float, default = 0.001,
                        help = " error threshold default = 0.0001")
    parser.add_argument("--iter", type = int, default = 100,
                        help = " Maximum Iterations default = 100")
    parser.add_argument("--plt", type = bool, default = False,
                        help = " Generate images of convergance. ~~~SLOW~~~")
    parser.add_argument("--save", type = bool, default = False,
                        help = " Save images of convergance.")	
    parser.add_argument("--erplt", type = bool, default = True,
                        help = "Generate graph with the Error Convergence")
    return parser.parse_args()

def main():
    args = cmdparser() # Parse settings
    fixed = pointParser(args.fix) # Load pointClouds
    moving = pointParser(args.mov)
    thres = args.thres
    maxIter = args.iter
    plotOrNot = args.plt
    savePlots = args.save
    errorPlot = args.erplt
    
    icp = IterativeClosestPoint(thres, maxIter, plotOrNot = plotOrNot, savePlots = savePlots)
    
    print('Starting... ')
    start = time.time()

    _,errStorage,_ = icp.register(fixed, moving)

    fin = time.time()
    print('\nDONE...')
    print('Total Time: {} s'.format(fin-start))
    
    '''Plot Error OR Not???'''
    if errorPlot == True:
            errplotter(errStorage)

if __name__ == "__main__":
    main()          