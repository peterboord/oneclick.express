def getUrl():
	#returnUrl = "https://www.yelp.com/biz/waitrose-wilmslow"
	#returnUrl = 'https://upload.wikimedia.org/wikipedia/commons/0/07/Emperor_Penguin_Manchot_empereur.jpg'
	import sys
	import os
	import numpy as np
	import cv2
	path_to_image_to_be_processed = '/home/pboord/Downloads/yelp/waitrose.jpg'
	pathname = '/home/pboord/Downloads/yelp'
	img = cv2.imread(path_to_image_to_be_processed)
	vis = img.copy()
	channels = cv2.text.computeNMChannels(img)
	cn = len(channels)-1
	for c in range(0,cn):
  		channels.append((255-channels[c]))
	for channel in channels:
  		erc1 = cv2.text.loadClassifierNM1(pathname+'/trained_classifierNM1.xml')
  		er1 = cv2.text.createERFilterNM1(erc1,16,0.00015,0.13,0.2,True,0.1)
  		erc2 = cv2.text.loadClassifierNM2(pathname+'/trained_classifierNM2.xml')
  		er2 = cv2.text.createERFilterNM2(erc2,0.5)
  		regions = cv2.text.detectRegions(channel,er1,er2)
  		rects = cv2.text.erGrouping(img,channel,[r.tolist() for r in regions])
  		for r in range(0,np.shape(rects)[0]):
    			rect = rects[r]
    			cv2.rectangle(vis, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (0, 0, 0), 2)
    			cv2.rectangle(vis, (rect[0],rect[1]), (rect[0]+rect[2],rect[1]+rect[3]), (255, 255, 255), 1)
	cv2.imwrite('waitrose_boxed.jpg',vis)		
	returnUrl = open('waitrose_boxed.jpg', 'rb').read().encode('base64').replace('\n', '')
	return returnUrl
