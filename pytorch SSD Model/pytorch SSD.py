import torch
import torchvision
from torchvision import transforms as T
import cv2
import cvzone


model = torchvision.models.detection.ssd300_vgg16(pretrained = True)
model.eval()


classnames = []
with open('classes.txt','r') as f:
    classnames = f.read().splitlines()

# print(classnames[0])

image = cv2.imread('dog2.jpg')
img = image.copy()
print(type(image))

imgtransform = T.ToTensor()
image = imgtransform(image)
print(type(image))

with torch.no_grad():
    ypred = model([image])
    print(ypred[0].keys())

    bbox,scores,labels = ypred[0]['boxes'],ypred[0]['scores'],ypred[0]['labels']
    nums = torch.argwhere(scores > 0.80).shape[0]
    for i in range(nums):
        x,y,w,h = bbox[i].numpy().astype('int')
        cv2.rectangle(img,(x,y),(w,h),(0,0,255),5)
        classname = labels[i].numpy().astype('int')
        classdetected = classnames[classname-1]
        # print(classdetected)
        cvzone.putTextRect(img,classdetected,[x,y+100],scale=2,border=2)

cv2.imshow('frame',img)
cv2.waitKey(0)