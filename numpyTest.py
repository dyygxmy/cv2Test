import numpy as np

# 数组的创建
# n1 = np.array([1,2,3]) #一维数组
# n2=np.array([[1,2],[3,4]]) #二维数组
# n3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) # 三维数组
# n4=np.array([1],ndmin=4) # 四维数组
# print(n1)
# print(n2)
# print(n3)
# print(n4)
# n_e=np.empty((2,3,2)) # 2行 3列 2通道的空数组
# print(n_e)
# n_0 = np.zeros((2, 2))
# n_1 = np.ones((2, 2),np.uint8)
# print(n_0)
# print(n_1)
r1=np.random.randint(0,2,5) # 一维数组
r2=np.random.randint(0,2,(2,2)) # 二维数组
r3=np.random.randint(0,2,(2,2,2)) # 三维数组
print(r1)
print(r2)
print(r3)



# 数组取值及切片
# n = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(n)
# print(n[:])
# print(n[:3])
# print(n[3:6])
# print(n[6:])
# print(n[-1])
# print(n[1:7:2])
# print(n[::-2]) # 步长为负数，就倒过来取值

# 数组的运算
# n1 = np.array([1, 2])
# n2 = np.array([3, 4])
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)
# print(n1 ** n2)
# print(n1 % n2)
# print(n2 % n1)
# print(n1 > n2)
# print(n1 < n2)

# 数组的复制
# n3 = np.array(n1)
# n4 = np.array(n1, copy=True)  # 副本
# n5 = n1.copy()
# print(n3)
# print(n4)
# print(n5)
