import cv2

img = cv2.imread('media/groupPic.jpg',1)
imgBlur = cv2.imread('groupBlur.jpg',1)

imgAll = cv2.hconcat([img, imgBlur])
cv2.imshow("Output",imgAll)
cv2.imwrite("blurPic.jpg",imgAll)

cv2.waitKey(0)
cv2.destroyAllWindows()
