# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 21:00:51 2014
using Python 2.7.3

SVD (low) K-rank approximation

@author: ce
"""

import numpy
import scipy
import matplotlib.pyplot as plt
import scipy.linalg
import Image

im = Image.open("10.jpg")
print im.size, im.bits, im.format

ima3 = array(im) 

print ima3.shape
# print ima[100,20,0]

ima = copy(ima3[:,:,0])
print ima.shape
# print ima[100,20]


##################################
# SVD K-rank approximation
##################################
U,S,V = svd(ima)

K = 10

ima_new = zeros([size(ima,0), size(ima,1)])

for k in range(K):
    ima_new = ima_new + S[k] * outer(U[:,k],V[k,:])


##################################
# visualize
##################################
plt.close("all")

# original
im.show()

# approximation
scipy.misc.toimage(ima_new).show()
# scipy.misc.imsave('outfile.jpg', ima_new)





