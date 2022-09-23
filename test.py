
import cv2
import numpy as np

'''
# 拼接图像
img = cv2.imread("marker13.png")
img_h = np.hstack((img,img,img)) # 参数是一个数组，将数组内所有图片水平拼接在一起
img_v = np.vstack([img,img]) # 垂直拼接
cv2.imshow("one img",img)
cv2.imshow("hstack img",img_h)
cv2.imshow("vstack img",img_v)
'''

# 创建图像
# 黑白图像用单通道
width = 200
height = 100
# img = np.zeros((height,width),np.uint8)
# img = np.ones((height,width),np.uint8)*255
# img[25:37,50:100] = 255 # 纵坐标25到37像素，横坐标50到100像素区域为白色
# for i in range(0,width,40): # 画出一条斑马线
#     img[:,i:i+20] = 255 # 从0开始到整个宽中，每40个像素为单位把左边20个像素一竖条画成白色
# 随机图像
# img = np.random.randint(256,size=(height,width),dtype=np.uint8) # 你一个电视机的雪花图像
# 彩色图像用三通道
img = np.ones((height,width,3),np.uint8)
img[:,:,0] = 255 # 蓝色

cv2.imshow("",img)

cv2.waitKey()
cv2.destroyAllWindows()