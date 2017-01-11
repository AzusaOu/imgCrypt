# v1.0.0 - 2017.01.11

import numpy
import cv2
import sys

def imgEncrypt(imgName, img, method='simple', psw='-'):
	imgSize = img.shape
	if method == 'simple':
		imgx = img.reshape((imgSize[1], imgSize[0], imgSize[2]))

	# cv2.imshow('getImage', imgx)
	if '.png' not in imgName:
		imgNamex = '(ec)'+imgName+'.png'
	else:
		imgNamex = '(ec)'+imgName
	cv2.imwrite(imgNamex, imgx)
	return imgx

def imgDecrypt(imgName, img, method='simple', psw='-'):
	imgSize = img.shape
	if method == 'simple':
		imgx = img.reshape((imgSize[1], imgSize[0], imgSize[2]))

	# cv2.imshow('getImage', imgx)
	if '.png' not in imgName:
		imgNamex = '(dc)'+imgName+'.png'
	else:
		imgNamex = '(dc)'+imgName
	cv2.imwrite(imgNamex, imgx)
	return imgx

def wait4exit():
	k = cv2.waitKey(0)
	if k == 27:
		cv2.destoryAllWindows()
	elif k == ord('s'):
		cv2.imwrite('02.png', img)
		cv2.destoryAllWindows()

def test():
	img = cv2.imread('hx.jpg')
	imgx = imgEncrypt(img)
	cv2.imshow('getImage', imgx)
	cv2.imshow('Decrypt', imgDecrypt(imgx))

if __name__ == '__main__':
	# test()
	# Format: python imgCrypt.py <img> <e/d> <method> [password]
	coo = sys.argv
	try:
		img = cv2.imread(coo[1])
		if len(coo) < 4 or len(coo) > 5:
			print('<img> <e/d> <method> [password]')
			sys.exit()
		if len(coo) == 4:
			coo.append('-')

		if coo[2] == 'e':
			imgEncrypt(coo[1], img, coo[3], coo[4])
		else:
			imgDecrypt(coo[1], img, coo[3], coo[4])
		wait4exit()
	except:
		print('Something error.')