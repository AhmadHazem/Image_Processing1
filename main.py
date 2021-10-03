import cv2 as cv

# do not forget to change the directory of the image

img = cv.imread('image.jpg')
cv.imshow('img', img)
cv.waitKey(0)
h, w = img.shape[:2]
center = (w // 2, h // 2)
matrix = cv.getRotationMatrix2D(center, -45, 1.0)
rotated = cv.warpAffine(img, matrix, (w, h))
cv.imshow('img', rotated)
cv.waitKey(0)
cropped_image = rotated[80 : 325, 80 : 325]
cv.imshow('img', cropped_image)
cv.waitKey(0)
img2 = cv.rectangle(cropped_image,(30,205),(205,235),(255,255,255),-1)
img3 = cv.putText(img2,'Ahmad Hazem',(40,225),cv.FONT_HERSHEY_TRIPLEX,0.6,(0,0,0),1)
cv.imwrite('FinalImg.jpg', img3)
cv.imshow('img',img3)
cv.waitKey(0)