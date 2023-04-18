import cv2
import matplotlib.pyplot as plt
import easyocr

image = cv2.imread('program.png')
read = easyocr.Reader(lang_list=['en'],gpu=True)

result = read.readtext(image)
for res in result:
    bbox,text,score = res
    cv2.rectangle(image,bbox[0],bbox[2],(255,0,0),5)
    print(bbox)



plt.imshow(image)
plt.show()