import urllib.request
import cv2
import numpy as np

def image_from_url(url):
	rep = urllib.request.urlopen(url).read()
	image = np.asarray(bytearray(rep), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

repertoire='negatives/'
lien_img="http://image-net.org/api/text/imagenet.synset.geturls?wnid=n14974264"

img_url=urllib.request.urlopen(lien_img).read().decode()
i=0

for url in img_url.split('\n'):
	try:	
		chemin=repertoire+'img'+str(i)+'.jpg'
		image=image_from_url(url)
		resized_image = cv2.resize(image, (100, 100))
		cv2.imwrite(chemin,resized_image)
		i+=1
	except:
		pass	
	
