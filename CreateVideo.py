import os
import cv2


path = "Images"

images = ['111.jpg', '112.jpg', '113.jpg', '114.jpg', '115.jpg', '116.jpg', '117.jpg', '118.jpg', '119.jpg', '120.jpg']


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
frame = cv2.imread(images[0])
size = (width,height)
count = len(images)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc('*DIVX'), 0.8,size)