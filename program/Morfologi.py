import matplotlib.pyplot as plt
import program.pcd as pcd
import numpy as np

img = plt.imread('../image/phone.png')

newImg = pcd.rgb2Gray(img)

newImg = pcd.biner(newImg, 90, 0, 90, 255)
# print(newImg)

temp = pcd.dilation(newImg, 3)
# temp = pcd.dilation(temp, 1)
# temp = pcd.dilation(temp, 1)
temp = pcd.erotion(temp, 3)
# temp = pcd.erotion(temp, 1)

# disk = pcd.disk(1)
# print(np.shape(disk))


# print(temp)


f = plt.figure()
f.add_subplot(1,2, 1)
plt.title("Original")
plt.imshow(newImg, cmap = plt.get_cmap('gray'))
f.add_subplot(1,2, 2)
plt.title("Gray")
plt.imshow(temp, cmap = plt.get_cmap('gray'))
plt.show();