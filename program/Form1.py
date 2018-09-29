import matplotlib.pyplot as plt
import program.pcd as pcd

img = plt.imread('../image/lena.png')

imgGray = pcd.rgb2Gray(img)

imgNegative = pcd.negative(imgGray)

imgLog = pcd.logTransformations(imgGray, 1)

imgPowLog = pcd.powerLawTransformation(imgGray, 1, 3)

imgCS = pcd.contrastStretching(img,20,40,80,150)

# imgBiner = pcd.biner(img, 80, 0, 80, 255)
# plt.imshow(imgBiner, cmap=plt.get_cmap('gray'))
# plt.show()

f = plt.figure()
f.add_subplot(2,3, 1)
plt.imshow(img, cmap = plt.get_cmap('gray'))
f.add_subplot(2,3, 2)
plt.imshow(imgGray, cmap = plt.get_cmap('gray'))
f.add_subplot(2,3, 3)
plt.imshow(imgNegative, cmap = plt.get_cmap('gray'))
f.add_subplot(2,3, 4)
plt.imshow(imgLog, cmap = plt.get_cmap('gray'))
f.add_subplot(2,3, 5)
plt.imshow(imgPowLog, cmap = plt.get_cmap('gray'))
f.add_subplot(2,3, 6)
plt.imshow(imgCS, cmap = plt.get_cmap('gray'))
plt.show()
