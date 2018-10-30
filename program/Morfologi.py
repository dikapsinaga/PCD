import matplotlib.pyplot as plt
import program.pcd as pcd

img = plt.imread('../image/phone.png')

newImg = pcd.rgb2Gray(img)


newImg = pcd.biner(newImg, 120,0,120,255)
# print(newImg)

temp = pcd.dilation(newImg)
# temp = pcd.dilation(temp)
# temp = pcd.dilation(temp)
# temp = pcd.erotion(temp)
# temp = pcd.erotion(newImg)



# print(temp)


f = plt.figure()
f.add_subplot(1,2, 1)
plt.title("Original")
plt.imshow(newImg, cmap = plt.get_cmap('gray'))
f.add_subplot(1,2, 2)
plt.title("Gray")
plt.imshow(temp, cmap = plt.get_cmap('gray'))
# plt.show();