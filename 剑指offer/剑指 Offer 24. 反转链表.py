# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        headPoint = head
        dataList = []
        while True:
            if head == None:
                break
            dataList.append(head.val)
            head = head.next
        dataList = dataList[::-1]
        resultPoint = headPoint
        for i in dataList:
            headPoint.val = i
            headPoint = headPoint.next
        return resultPoint