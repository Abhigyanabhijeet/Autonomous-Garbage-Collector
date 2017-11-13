import cv2
import imutils
import numpy as np
import os
from collections import OrderedDict
from scipy.spatial import distance as dist

def colorDetect(image, c):
	# Include this function in the main code
	# later. This is to detect the color of the garbage.
	colors = OrderedDict({
			"red": (255, 0, 0),
			"green": (0, 255, 0),
			"blue": (0, 0, 255)})

	lab = np.zeros((len(colors), 1, 3), dtype="uint8")
	colorNames = []

	for (i, (name, rgb)) in enumerate(colors.items()):
		# update the L*a*b* array and the color names list
		lab[i] = rgb
		colorNames.append(name)

	lab = cv2.cvtColor(lab, cv2.COLOR_RGB2LAB)

	mask = np.zeros(image.shape[:2], dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	mask = cv2.erode(mask, None, iterations=2)
	mean = cv2.mean(image, mask=mask)[:3]

	minDist = (np.inf, None)

	for (i, row) in enumerate(lab):
		d = dist.euclidean(row[0], mean)

		if d < minDist[0]:
				minDist = (d, i)

	return colorNames[minDist[1]]

def saveRefImg(event, x, y, img_saved, img_gray):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.imwrite('ref.png', img_gray)
		print ("Yes! You captured the reference image.")

def main():
	maxArea = 1000000000

	# Taking reference image first.
	print ("Let's capture the reference image first. This is an image of the room/background.")
	print ("Please setup the camera properly and double click on the image to save the image as the reference image.")

	if (os.path.isfile('ref.png')):
		os.remove('ref.png')
		print ("File already found. File now deleted.")

	cam = cv2.VideoCapture(1)
	cv2.namedWindow('Reference Image', cv2.WINDOW_AUTOSIZE)

	while True:
		ret, img = cam.read()

		cv2.imshow('Reference Image', img)

		cv2.setMouseCallback('Reference Image', saveRefImg, img)

		refImgFlag = os.path.isfile('ref.png')

		if refImgFlag:
			print ("Image Saved")
			break

		k = cv2.waitKey(30) & 0xff

		if k == 27:
			break

	cv2.destroyAllWindows()

	camera = cv2.VideoCapture(1)

	while True:
		grabbed, img = camera.read()

		if not grabbed:
			print ("Cound not open the camera.")
			break

		refImg = cv2.imread('ref.png')
		refImgResized = imutils.resize(refImg, width=720)
		refImgCopy = refImgResized.copy()
		refImgRatio = refImg.shape[0] / float(refImgResized.shape[0])

		# img = cv2.imread('garbage_new.jpg')
		imgResized = imutils.resize(img, width=720)
		imgCopy = imgResized.copy()
		imgRatio = img.shape[0] / float(imgResized.shape[0])

		refImgResizedBlurred = cv2.GaussianBlur(refImgResized, (5, 5), 0)
		imgResizedBlurred = cv2.GaussianBlur(imgResized, (5, 5), 0)

		refImgGray = cv2.cvtColor(refImgResizedBlurred, cv2.COLOR_BGR2GRAY)
		# cv2.imshow('refImgGray', refImgGray)
		# cv2.waitKey(0)
		imgGray = cv2.cvtColor(imgResizedBlurred, cv2.COLOR_BGR2GRAY)
		# cv2.imshow('imgGray', imgGray)
		# cv2.waitKey(0)

		imgLab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

		absDiff = cv2.absdiff(imgGray, refImgGray)
		# cv2.imshow('AbsDiff', absDiff)
		# cv2.waitKey(0)

		thresh = cv2.threshold(absDiff, 25, 255, cv2.THRESH_BINARY)[1]
		# cv2.imshow('Thresh', thresh)
		# cv2.waitKey(0)

		threshDilated = cv2.dilate(thresh, None, iterations=2)
		# cv2.imshow('ThreshDilated', threshDilated)
		# cv2.waitKey(0)

		contours2 = []

		q, contours, _ =  cv2.findContours(threshDilated, 
					cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

		for (i, c) in enumerate(contours):
			if( cv2.contourArea(c) < maxArea):
				contours2.append(c)

		contours = contours2

		for c in contours:
			# compute the center of the contour
			M = cv2.moments(c)
			#cX = int((M["m10"] / M["m00"]) * ratio)
			cX = int(M["m10"] / M["m00"])
			#cY = int((M["m01"] / M["m00"]) * ratio)
			cY = int(M["m01"] / M["m00"])

			# detect and label the color
			color = colorDetect(imgLab, c)

			# multiply the contour (x, y)-coordinates by the resize ratio,
			# then draw the contours and the name of the shape and labeled
			# color on the image
			c = c.astype("float")
			# c *= ratio
			c = c.astype("int")
			text = "{}".format(color)
			cv2.drawContours(imgCopy, [c], -1, (0, 255, 0), 2)
			cv2.putText(imgCopy, text, (cX, cY),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

			# show the output image
			cv2.imshow("Image", imgCopy)
			# cv2.waitKey(0)

		k = cv2.waitKey(1) & 0xFF

		if k == 27:
			break

if __name__ == "__main__":
	main()
