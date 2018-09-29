import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as ndi

img1 = ndi.imread('../img/baboon.png')
img2 = plt.imread('../img/lena.png')



Rlena = img1[:,:,0]
Rlena = img1[:,:,1]
Rlena = img1[:,:,2]



#processing image
#negative
# img = 255 - img

#div by 2 // penggelapan
# img = 0.5 * img

# gray


# biner


#sum // overlapping
img3 = 0.7*img1 + 0.3*img2
plt.imshow(img3)
plt.show()