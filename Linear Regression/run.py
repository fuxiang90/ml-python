# coding=utf-8
#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import mlpy

ex2_path_x = '/home/fuxiang/data/machine learning/ex2x.dat'

ex2_path_y = '/home/fuxiang/data/machine learning/ex2y.dat'


def get_input():
    fx = open(ex2_path_x)

    x =[] 
    for each in fx:
        x.append(float( each) )
#     print x
    
    fy = open(ex2_path_y)
    y =[] 
    for each in fy:
        y.append(float( each) )
#     print x

    return x ,y
    

def main():
    
    x ,y = get_input()
#     print x
#     print y
#     
#     
    plt.figure()
 
    plt.plot(x,y,'*')
    plt.xlabel('Height in meters')
    plt.ylabel('Age in years')
     
    plt.legend()
    plt.show()
     
   
    
#     new_arr = [1 for i in range(0,len(x))]
#     print new_arr
#     new_arr.extend(x)
#     npx = np.array(x)
#     d = npx.reshape(2,len(x))
# 
#     print npx
    #### 
    new_x = []
    for each in x:
        a = []
        a.append(1)
        a.append(each)
        new_x.append(a)
        new_x 
    print new_x
    
    mlpy_linear_regressiono(new_x,y)

    pass

def mlpy_linear_regressiono(x ,y):
    beta ,rank = mlpy.ols_base(x, y,0.05)
    
    
    test_x = [[1,3.5] ,[1,7]]
    
    for each in test_x:
        test_y = beta[0] *each[0] + beta[1]*each[1]
        print test_y
    print beta
    
    plot_x = np.arange(min(x),max(x))
    plot_y = [beta[0] + beta[1]*i for i in x ]
    
    plt.plot(plot_x,plot_y)
    plt.show()
if __name__ == '__main__':
    main()
    
    print "done it"