# # -*- coding:UTF-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt
#
# """
# 函数作用：读取数据
#
# parameter：
#     fileName:数据文件
# """
# def loadDataSet(fileName):
#     # 初始化空列表
#     dataSet = []
#     # 读取数据文件
#     fr = open(fileName)
#     # 遍历每一行
#     for line in fr.readlines():
#         linArr = line.strip().split("\t")
#         # print(linArr)
#         fltLine = list(map(float, linArr))  # 将字符串元素转换为浮点型,python3中map需要和list搭配使用
#         dataSet.append(fltLine)
#     return np.mat(dataSet)
#
#
# """
# 函数作用：欧式距离
#
# Paramter：
#     vecA:
#     vecB:
# """
#
#
# def distEclud(vecA, vecB):
#     dis = np.sqrt(np.sum(np.power(vecA - vecB, 2)))
#     return dis
#
#
# """
# 函数：随机初始化质心
#
# paramter:
#     dataMat：样本数据矩阵
#     K:质心个数
# """
#
#
# def randCent(dataMat, k):
#     # 获取样本矩阵的长宽
#     m, n = dataMat.shape
#     centroids = np.mat(np.zeros((k, n)))
#     # print(dataMat)
#     for i in range(n):
#         minJ = min(dataMat[:, i])
#         maxJ = max(dataMat[:, i])
#         rangJ = float(maxJ - minJ)
#         centroids[:, i] = np.mat(minJ + rangJ * (np.random.rand(k, 1)))
#     print(centroids)
#     return centroids
#
#
# """
# 函数：K-Means算法的实现
# parameter:
#     dataMat:样本数据矩阵
#     K:质心数量
#     distMeas:欧式距离函数
#     createCent:初始化质心
#
# """
#
#
# def kMeans(dataMat, k, distMeas=distEclud, createCent=randCent):
#     # 获取样本矩阵的维度
#     m, n = dataMat.shape
#     # 第二列存储误差
#     clusterAssment = np.mat(np.zeros((m, 2)))
#     # 初始化质心
#     centroids = createCent(dataMat, k)
#     # 初始化标志向量，用于判断是否继续进行迭代，如果为true，则继续迭代
#     clusterChanged = True
#     while clusterChanged:
#         clusterChanged = False
#
#         for i in range(m):
#             minDist = 9999999
#             minIndex = -1
#
#             for j in range(k):
#                 distJI = distMeas(centroids[j, :], dataMat[i, :])
#                 if distJI < minDist:
#                     minDist = distJI
#                     minIndex = j
#             if clusterAssment[i, 0] != minIndex:
#                 clusterChanged = True
#             clusterAssment[i, :] = minIndex, minDist ** 2
#         for cent in range(k):
#             ptsInClust = dataMat[np.nonzero(clusterAssment[:, 0].A == cent)[0]]
#             centroids[cent, :] = np.mean(ptsInClust, axis=0)
#     return centroids, clusterAssment
#
#
# """
# 函数：可视化数据
# """
#
#
# def showCluster(dataSet, k, centroids, clusterAssment):
#     # 新建一个画布
#     fig = plt.figure()
#     plt.title("k-means")
#     ax = fig.add_subplot(111)
#     data = []
#     for cent in range(k):
#         ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == cent)[0]]
#         data.append(ptsInClust)
#     for cent, c, maker in zip(range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's']):
#         ax.scatter(data[cent][:, 0].tolist(), data[cent][:, 1].tolist(), s=30, c=c, marker=maker)
#     ax.scatter(np.array(centroids)[:, 0].tolist(), np.array(centroids)[:, 1].tolist(), s=100, c='black', marker='+',
#                alpha=1)
#     ax.set_xlabel("X")
#     ax.set_ylabel("Y")
#     plt.show()
#
#
# ###mian函数###
# if __name__ == '__main__':
#     dateLoad = loadDataSet("test.txt")
#     centr, clA = kMeans(dateLoad, 4, distEclud, randCent)
#     showCluster(dateLoad, 4, centr, clA)
# -*- coding:utf-8 -*-
#Definition for singly-linked list.
import sys


# 定义节点
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


# 定义链表
class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head
        while node != None:
            print(node.value, end=' ')
            node = node.next


class Solution:
    def twosum(self, l1, l2):
        temp = ListNode(0)
        l3 = temp
        a = 0
        while l1 != None or l2 != None or a != 0:
            if l1 != None:
                a += l1.value
                l1 = l1.next
            if l2 != None:
                a += l2.value
                l2 = l2.next
            temp.next = ListNode(a % 10)
            temp = temp.next
            a = a // 10
        return l3.next


if __name__ == "__main__":

    l3 = [1,2,4]
    l4 = [2,5,2]
    b = LinkList()
    l1 = b.initList(l3)
    l2 = b.initList(l4)
    a = Solution()
    l5 = a.twosum(l1, l2)
    b.printlist(l5)



