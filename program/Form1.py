import matplotlib.pyplot as plt
import program.pcd as pcd

img = plt.imread('../image/lena.png')

imgGray = pcd.rgb2Gray(img)

imgNegative = pcd.negative(imgGray)

imgLog = pcd.logTransformations(imgGray, 1)

imgPowLaw = pcd.powerLawTransformation(imgGray, 1, 3)

imgCS = pcd.contrastStretching(img,20,40,80,150)

imgBiner = pcd.biner(img, 80, 0, 80, 255)

imgGrayLevelSlicing = pcd.grayLevelSlicing(img)

f = plt.figure()
f.add_subplot(3,3, 1)
plt.title("Original")
plt.imshow(img, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 2)
plt.title("Gray")
plt.imshow(imgGray, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 3)
plt.title("Negative")
plt.imshow(imgNegative, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 4)
plt.title("Log Trans")
plt.imshow(imgLog, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 5)
plt.title("Pow Law Trans")
plt.imshow(imgPowLaw, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 6)
plt.title("Contras Streching")
plt.imshow(imgCS, cmap = plt.get_cmap('gray'))
f.add_subplot(3,3, 7)
plt.title("Binerisasi")
plt.imshow(imgBiner, cmap=plt.get_cmap('gray'))

f.add_subplot(3,3, 8)
plt.title("imgGrayLevelSlicing")
plt.imshow(imgGrayLevelSlicing, cmap=plt.get_cmap('gray'))

plt.show()
