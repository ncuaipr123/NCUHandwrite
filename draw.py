import numpy as np
import cv2
import os
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

def DrawDots2D(dots,hw=(600,800)):
    img=np.zeros((hw[0],hw[1],3),np.uint8)+255
    for xyz in dots:
        try:x,y,z=xyz
        except:x,y=xyz
        x=int(x*hw[1])
        y=int(y*hw[0])
        cv2.circle(img,(x,y),1,(219,147,43),4)
    return img

def DrawDots3D(dots,hw=(600,800),show=False):
    figsize=(hw[1]/100,hw[0]/100)
    fig=pyplot.figure(figsize=figsize,dpi=100)
    ax=Axes3D(fig)
    
    dots=np.array(dots)
    x_arr=dots[...,0]
    y_arr=1-dots[...,1]
    try:z_arr=dots[...,2]
    except:z_arr=np.ones(x_arr.shape)
    ax.scatter(x_arr,y_arr,z_arr)
    if(show==True):pyplot.show()
    else:fig.canvas.draw()
    img=np.frombuffer(fig.canvas.tostring_rgb(),dtype=np.uint8)
    img=img.reshape(fig.canvas.get_width_height()[::-1]+(3,))
    img=img[...,::-1]
    return img
