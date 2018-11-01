import matplotlib.pyplot as plt
import program.pcd as pcd
import numpy as np
import PIL

# img = plt.imread('../image/koin.png')
img = PIL.Image.open('../image/leaf2.jpg')

arr = np.array(img)
newImg = pcd.rgb2Gray(arr)

# newImg = pcd.logTransformations(newImg, 1.3)
newImg = pcd.biner(newImg, 127, 0, 127, 255)


# temp = pcd.dilation(newImg, 3)
# temp = pcd.dilation(temp, 1)
# temp = pcd.dilation(temp, 1)
temp = pcd.erotion(newImg, 3)
temp = pcd.erotion(temp, 3)


f = plt.figure()
f.add_subplot(1,2, 1)
plt.title("Original")
plt.imshow(newImg, cmap = plt.get_cmap('gray'))
f.add_subplot(1,2, 2)
plt.title("Gray")
plt.imshow(temp, cmap = plt.get_cmap('gray'))
plt.show();