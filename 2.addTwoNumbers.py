# -*- coding:utf-8 -*-
#Definition for singly-linked list.
#定义节点
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#定义链表
class Linklist(object):
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = ListNode(data[0])  #是一个链表节点给头
        n = m = self.head  #临时存

        for i in data[1:]:
            node = ListNode(i)
            n.next = node
            n = n.next
        return m

    def printList(self, head):
        if not head:
            return
        node = head
        while node!= None:   #node 可以next next的不断取值  普通列表用for循环迭代
            print(node.val,end=' ')
            node = node.next   #node往前走一个

class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:
        """
        #首先创建一个虚拟节点，并创建一个current指针，指向这个节点
        current = dummy = ListNode()
        #初始化carry和两个链表对应节点相加的值
        carry, value = 0, 0
        #下面的while循环中之所以有carry，是为了处理两个链表最后节点相加出现进位的情况
        #当两个节点都走完而且最后的运算并没有进位时，就不会进入这个循环
        while carry or l1 or l2:
            #让value先等于carry既有利于下面两个if语句中两个对应节点值相加，
            # 也是为了要处理两个链表最后节点相加出现进位的情况
            value = carry
            #只要其中一个链表没走完，就需要计算value的值
            #如果其中一个链表走完，那么下面的计算就是加总carry和其中一个节点的值
            #如果两个链表都没走完，那么下面的计算就是carry+对应的两个节点的值
            if l1: l1, value = l1.next, l1.val + value
            if l2: l2, value = l2.next, l2.val + value
            #为了防止value值大于十，出现进位，需要特殊处理
            #如果value小于十，下面这行的操作对于carry和value的值都没有影响
            carry, value = divmod(value, 10)
            #利用value的值创建一个链表节点，并让current.next指向它
            current.next = ListNode(value)
            #移动current指针到下一个节点
            current = current.next
        #最后只要返回dummy的下一个节点就是我们想要的答案。
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    test_list1 = [1, 2, 3, 8]
    test_list2 = [2, 3, 4, 3]
    b = Linklist()
    test1 = b.initList(test_list1)
    test2 = b.initList(test_list2)

    test_output = s.addTwoNumbers(test1, test2)
#    b.printList(test_output)

    #test_list2 = ListNode()
   # test_list2.val = 3
    #test_list2.next = [4, 4]
    # test_list2(2, 4)
    # head = test_output
    # if not head:
    #
    while test_output != None:
        print(test_output.val)
        test_output = test_output.next

