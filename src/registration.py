''' 
                                    *********************
                                    *      ICP-SVD      *
                                    *                   *
                                    *                   *
                                    *      Kyriakos     *
                                    *      Lite         *
                                    *                   *
                                    *********************

This is an implementation of a Signular Value Decomposition (SVD) - based,  Iterative Closest Point (ICP) cloud registration algorithm.
The algorithm utilizes KDTree from scipy.spatial to speed up point-to-point distance measurements and find point correspondences.
'''

import numpy as np
import matplotlib.pyplot as plt
from src.utils import plotClouds
from scipy.spatial import cKDTree as KDTree

class IterativeClosestPoint():
    """Class for the ICP-SVD algorithm.
    """    
    def __init__(self, thres, maxIter, plotOrNot = False, savePlots = False):
        """Initializes the ICP-SVD algorithm.

        Args:
            thres (float): Error threshold.
            maxIter (int): Maximum number of iterations.
            plotOrNot (bool, optional): Plot evolution of point clouds. Defaults to False.
            savePlots (bool, optional): Save the plots. Defaults to False.
        """        
        self.thres = thres
        self.maxIter = maxIter
        self.plotOrNot = plotOrNot
        self.savePlots = savePlots

# Calculates the centroid of the corresponding points of the fixed cloud
    def indxtMean(self, index, cloud):    
        indxSum = np.array([0.0, 0.0 ,0.0])
        nPoints = np.size(index, 0)
        for i in range(nPoints):
            indxSum = np.add(indxSum, np.array(cloud[index[i]]), out = indxSum ,casting = 'unsafe')

        return indxSum/nPoints
    
# Extract specific points from a point cloud based on given indices
    def indxtFixed(self, index, cloud):
        T = []
        for i in index:
            T.append(cloud[i])
            
        return np.asanyarray(T)

# Implementation of the registration algorithm    
    def register(self, fixed, moving):
        finhom = np.identity(4)
        reqR = np.identity(3)
        reqT = [0.0, 0.0, 0.0]
        TREE = KDTree(fixed)
        n = np.size(moving,0)
        preverr, err = np.inf, np.inf
        errStorage = []
        iter = 0

        
        while True:
            iter += 1
            preverr = err
            distance, index = TREE.query(moving)
            
            err = np.mean(distance**2) #Calculate and store the Error
            errStorage.append(err)

            com = np.mean(moving,0) #Centroid of moving (com) point cloud
            cof = self.indxtMean(index, fixed) #Centroid of fixed(cof) point cloud

            W = np.dot(np.transpose(moving), self.indxtFixed(index, fixed)) - n*np.outer(com,cof) 
            U , _ , V  = np.linalg.svd(W, full_matrices = False) 
            tempR = np.dot(V.T,U.T) #Form the rotation matrix
            tempT = cof - np.dot(tempR,com) #Form the translation vector

            moving = (tempR.dot(moving.T)).T #Apply roto-translation
            moving = np.add(moving,tempT)

            reqR=np.dot(tempR,reqR) #Save roto-translation
            reqT = np.add(np.dot(tempR,reqT),tempT)
            print('Cycle {} the MSE is equal to {}'.format(iter, round (err, 5)))

            if self.plotOrNot or self.savePlots: #Plot/Save the point clouds
                plotClouds(fixed, moving, iter, self.plotOrNot, self.savePlots)

            if (preverr < err) or err < self.thres: #Exit condition
                finhom[0:3,0:3] = reqR[0:,0:] #Create a Homogeneous Matrix of the Results
                finhom[0:3,3] = reqT[:]

                print('\nThe Algorithm has exited on the {}th iteration with Error: {}\n'.format(iter, err))
                print('The Homogeneous Transformation matrix =\n \n {}'.format(finhom))
                break # breaks the for loop

        finhom[0:3,0:3] = reqR[0:,0:] #Create a Homogeneous Matrix of the Results
        finhom[0:3,3] = reqT[:]
        return finhom, errStorage, moving
                             
if __name__ == "__main__":
    print('ICP-SVD Algorithm')          	
