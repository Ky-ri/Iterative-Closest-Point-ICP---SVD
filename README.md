![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
# Iterative Closest Point(ICP)

Algorith implementation to register 2 point clouds using singular value decomposition(SVD) utilizing KDTree from scipy.spatial
```bash

Iterative-Closest-Point-ICP---SVD/
│   └── GIF.gif
│   └── GIF2.gif
│   └── errorConv.png
│   └── README.md
│   └── LICENSE
│
│── examples/ # Three simple examples.
│   └── example1.py
│   └── example2.py
│   └── example3.py
│
│── pointClouds/ # Two misaligned point clouds.
│   └── point_cloud_a.txt
│   └── point_cloud_b.txt
│
│── src/ 
│   └── oper.py # Rotation Matrices
│   └── registration.py # ICP
│   └── utils.py # Visualization & parcing
│   └── __init__.py
```
## Requirements
- [Python >=3.10.x](https://www.python.org/)
- [numpy](https://numpy.org/)
- [scipy](https://scipy.org/)
- [matplotlib](https://matplotlib.org/)

## Usage
**Example 1**: Register two point clouds. Settings specified via terminal/cmd.<br><br>
cd Iterative-Closest-Point-ICP---SVD<br>
python examples\example1.py --fix 'pointClouds\point_cloud_a.txt' --mov 'pointClouds\point_cloud_b.txt'<br><br>
**Options**:<br>
**--fix**: filename of fixed point point cloud.<br>
**--mov**: filename of moving point point cloud.<br>
**--thres**: error threshold default = 0.001.<br>
**--iter**: Maximum Iterations default = 100.<br>
**--plt**: Generate images of convergance.<br>
**--save**: Save images of convergance.	<br>
**--erplt**: Generate graph with the Error Convergence.<br><br>

**Example 2**: Register two point clouds. Settings specified in main().<br>

**Example 3**: Register two point clouds. Apply a user defined cloud roto-translation on an existing point and register.<br>

## References
1: http://ais.informatik.uni-freiburg.de/teaching/ss11/robotics/slides/17-icp.pdf<br>
2: https://www.ipb.uni-bonn.de/html/teaching/msr2-2020/sse2-03-icp.pdf<br>
3: https://en.wikipedia.org/wiki/Point-set_registration<br>

![alt text](https://github.com/KoulisL/Iterative-Closest-Point-ICP---SVD/blob/master/GIF.gif)
![Image](https://github.com/KoulisL/Iterative-Closest-Point-ICP---SVD/blob/master/errorConv.png)
![alt text](https://github.com/KoulisL/Iterative-Closest-Point-ICP---SVD/blob/master/GIF2.gif)
<hr>
<hr>

## License
[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

