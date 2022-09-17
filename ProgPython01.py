import numpy as np
import cv2 as cv
import cv2
import numpy as np
import cv2 as cv
def DelimitarCirculo (img):
	"""
	Genera como resultado una imagen con el resto del fondo eliminado 
	"""
	# convert the image to grayscale format
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	TamFiltro=3
	img_gray = cv.filter2D(img_gray,-1,np.ones((TamFiltro,TamFiltro),np.float32)/(TamFiltro*TamFiltro))
	# apply binary thresholding
	#ret, thresh = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	ret, thresh = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
	# visualize the binary image
	cv2.imshow('Binary image', thresh)
	IteracionesDilatacionErosion=5
	img_dilation = cv2.dilate(thresh, np.ones((5,5), np.uint8), iterations=IteracionesDilatacionErosion)
	img_dilation = cv2.erode(img_dilation, np.ones((5,5), np.uint8), iterations=IteracionesDilatacionErosion)
	masked = cv2.bitwise_and(img,img,mask=img_dilation)
	return (masked)
img = cv.imread('CuadranteA.jpg')
