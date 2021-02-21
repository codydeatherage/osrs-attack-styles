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

def crop_image(img, path, file):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(gray, 50, 100, cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnt = contours[0]
	x,y,w,h = cv2.boundingRect(cnt)
	crop = img[y:y+h,x:x+w]
	cv2.imshow('crop', crop)
	cv2.waitKey(0)
	#exec(crop, 'acc', path)
	cv2.imwrite(path + file + '_crop.png', crop)
weap_type = 'bow'

# img1 = cv2.imread(r"attackStyles\bows\bow_acc.png")
# img2 = cv2.imread(r"attackStyles\bows\bow_long.png")
# img3 = cv2.imread(r"attackStyles\bows\bow_rapid.png")

test_img = cv2.imread(r"attackStyles/bow/bow_acc.png")
path = 'C:/Users/Deatherage/Documents/python_work/image/attackStyles/' + weap_type + '/'
#crop_image(test_img, path)




	

#cv2.imshow('result', crop_image(test_img, 0))
#img4 = cv2.imread(r"attackStyles\bows\axe_block_t.png")

# exec(img1, "acc")
# exec(img2, "long")
# exec(img3, "rapid")
allTypes = []
path = 'C:/Users/cdeat/Documents/Practice/osrs-attack-styles/'
for filename in os.listdir(path):
	#if(filename.endswith(".png")):
	if(allTypes.count(filename) == 0 and not filename.endswith('.txt') and not filename.endswith('.PNG')):
		allTypes.append(filename)
	#print(os.path.join('C:/Users/cdeat/Documents/Practice/osrs-attack-styles/', filename))

print('OS Path', os.path)
for parentFile in allTypes:
	if(not parentFile.endswith('.py') and not parentFile.endswith('.md')):
	 	for filename in os.listdir(path + parentFile):
	 		if( '_sel' in filename):
	 			#
	 			img = cv2.imread(filename)
	 			newPath = path + parentFile +'/'+ filename
	 			splitFile = filename.split('.PNG')
	 			crop_image(cv2.imread(rf"{newPath}"), path + parentFile + '/', splitFile[0])
	 			#               print(f"{newPath}")
	 			
	 			# print(filename.split('PNG'))
	 			# print(path + parentFile + '/' + splitFile[0])
	 		#if(filename.count('_sel') > 0 and filename.endswith('.png')):
	 			
print('allTypes: ', allTypes)

# hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower = np.array([0, 0, 0])
# upper = np.array([200, 200, 200])
# masking = cv2.inRange(hsv_img, lower, upper)
# cv2.imshow('og', img)
# cv2.imshow("Mask", masking)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 