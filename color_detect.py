import cv2 
import numpy as np
import os

def exec(img, style, path):
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower = np.array([0, 0, 0])
	upper = np.array([200, 200, 200])
	masking = cv2.inRange(hsv_img, lower, upper)
	cv2.imshow('og', img)
	cv2.imshow("Mask", masking)
	#path = 'C:/Users/Deatherage/Documents/python_work/image/attackStyles/bow/'
	cv2.imwrite(path + style + "_mask.png", masking)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def crop_image(img, path):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	x,y,w,h = cv2.boundingRect(cnt)
	crop = img[y:y+h,x:x+w]
	# cv2.imshow('crop', crop)
	# cv2.waitKey(0)
	exec(crop, 'acc', path)
	#cv2.imwrite("C:/Users/Deatherage/Documents/python_work/image/attackStyles/bow/testtest.png", crop)
weap_type = 'bow'

# img1 = cv2.imread(r"attackStyles\bows\bow_acc.png")
# img2 = cv2.imread(r"attackStyles\bows\bow_long.png")
# img3 = cv2.imread(r"attackStyles\bows\bow_rapid.png")

test_img = cv2.imread(r"attackStyles/bow/bow_acc.png")
path = 'C:/Users/Deatherage/Documents/python_work/image/attackStyles/' + weap_type + '/'
crop_image(test_img, path)




	

#cv2.imshow('result', crop_image(test_img, 0))
#img4 = cv2.imread(r"attackStyles\bows\axe_block_t.png")

# exec(img1, "acc")
# exec(img2, "long")
# exec(img3, "rapid")
allTypes = []
path = 'C:/Users/Deatherage/Documents/python_work/image/attackStyles/'
for filename in os.listdir(path):
	#if(filename.endswith(".png")):
	if(allTypes.count(filename) == 0 and not filename.endswith('.txt') and not filename.endswith('.PNG')):
		allTypes.append(filename)
	print(os.path.join('C:/Users/Deatherage/Documents/python_work/image/attackStyles/', filename))

print('OS Path', os.path)
# for parentFile in allTypes:
# 	if()
print('allTypes: ', allTypes)

# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower = np.array([0, 0, 0])
# upper = np.array([200, 200, 200])
# masking = cv2.inRange(hsv_img, lower, upper)
# cv2.imshow('og', img)
# cv2.imshow("Mask", masking)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 