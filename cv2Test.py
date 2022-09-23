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
# img = np.ones((height,width,3),np.uint8)
# img[:,:,0] = 255 # 蓝色


# 设置图片透明效果
# img = cv2.imread("marker13.png")
# dst = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA) # 三通道转四通道
# dst[:,:,3] = 255/2 # 修改第四通道的值 0为全透明 255为不透明 255/2为半透明
# cv2.imshow("dst",dst) # imshow这个方法看不出透明效果
# cv2.imwrite("dst.png",dst) #保存图片就能看到效果了


# 设置图片曝光及过饱和效果
# img = cv2.imread("marker13.png")
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)  # 拆分出来
# s[:, :] = 255  # 饱和度调到最大
# # v[:,:]=255 #亮度调到最大
# hsv = cv2.merge([h, s, v])  # 再合并回去
# cv2.imshow("hsv", hsv)  # 直接看效果不明显，直接发红了，因为图片是bgr的
# out = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  # 再由hsv转换成bgr
# cv2.imshow("out", out)  # 这次显示就是发白了


#合并及拆分通道
# img = cv2.imread("flowers.png")
# b,g,r=cv2.split(img) #原图是bgr的色彩空间
# cv2.imshow("b",b) #黑白图，蓝通道占比多的就白些，少的地方就黑些
# cv2.imshow("g",g)#黑白图，绿通道占比多的就白些，少的地方就黑些
# cv2.imshow("r",r)#黑白图，红通道占比多的就白些，少的地方就黑些
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #bgr转hsv
# h,s,v=cv2.split(hsv)
# cv2.imshow("h",h) #黑白图，很模糊，失真
# cv2.imshow("s",s) #黑白图，饱和度也就是颜色越浓的地方越亮
# cv2.imshow("v",v)#黑白图，这个图更偏向我们平时看到的彩色转黑白图片，颜色越浅也就是越白的地方越亮


#操作图片像素的BGR值
img = cv2.imread("flowers.png")
print(img[100,100]) #该处的像素值为[47 67 77]
print(img[100,100,0])#b一通道的像素值为47
print(img[100,100,1])#g二通道的像素值为67
print(img[100,100,2])#r三通道的像素值为77

# cv2.imshow("",img)
cv2.waitKey() # 参数为等待时间为毫秒 不写时间就等到当按下任意按键时
cv2.destroyAllWindows()  # 销毁所有正在显示图像的窗口以释放内存
