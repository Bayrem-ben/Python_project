import cv2
import imutils
image = cv2.imread("image.png")

#cv2.imshow("image originale",image)
(h,w,d)=image.shape
print("width={},height{}=,depth={}".format(w,h,d))
#resize image
image=cv2.resize(image,(1400,800))
cv2.imshow("resized image",image)
#gray image conversion
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",gray)
#applying edge detection
edged = cv2.Canny(gray , 50, 255)
cv2.imshow("edged image",edged)
#threshholding
thresh=cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh image",thresh)
#contour detection

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output=image.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Contours",output)
text="I found {} objects !".format(len(cnts))
cv2.putText(output,text,(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(240,0,159),2)
cv2.imshow("Contours",output)

