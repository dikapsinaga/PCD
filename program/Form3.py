
import matplotlib.pyplot as plt
import program.pcd as pcd


tempA = plt.imread('../image/object1.png')
tempB= plt.imread('../image/object2.png')

tempA = pcd.rgb2Gray(tempA)
tempB = pcd.rgb2Gray(tempB)

newTemp = pcd.substraction(tempA, tempB)
newTemp1 = pcd.bitwiseAnd(tempA, tempB)
newTemp2 = pcd.bitwiseOr(tempA, tempB)
newTemp3 = pcd.bitwiseXOR(tempA, tempB)


f = plt.figure()
f.add_subplot(1,6, 1)
plt.imshow(tempA, cmap = plt.get_cmap('gray'))
f.add_subplot(1,6, 2)
plt.imshow(tempB, cmap = plt.get_cmap('gray'))
f.add_subplot(1,6, 3)
plt.imshow(newTemp, cmap = plt.get_cmap('gray'))
f.add_subplot(1,6, 4)
plt.imshow(newTemp1, cmap = plt.get_cmap('gray'))
f.add_subplot(1,6, 5)
plt.imshow(newTemp2, cmap = plt.get_cmap('gray'))
f.add_subplot(1,6, 6)
plt.imshow(newTemp3, cmap = plt.get_cmap('gray'))
plt.show()
