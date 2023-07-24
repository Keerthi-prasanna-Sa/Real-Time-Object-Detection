import cv2


myimage = cv2.imread("yug.png",-1)

#--------for resize the image----------
myimage = cv2.resize(myimage,(240,240))

#--------for flip the image----------
myimage = cv2.flip(myimage,2)

# print(myimage)
cv2.imshow("Imageviewer",myimage)


#----------wait while image is presenting------------- 
k = cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("D:\\output.png",myimage)
else:
# ----------distroy all the memory variables and windows
    cv2.destroyAllWindows()