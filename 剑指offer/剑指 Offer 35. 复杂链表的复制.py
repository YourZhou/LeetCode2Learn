"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class MySolution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pointList = []
        nodeRandom = []
        head2 = Node(0)
        backHead2 = head2
        backHead3 = head2
        while True:
            if head == None:
                break
            node = Node(head.val)
            head2.next = node
            pointList.append(node)
            nodeRandom.append(head.random)
            head = head.next
            head2 = head2.next
        backHead2 = backHead2.next
        for i in range(len(pointList)):
            if not nodeRandom[i] == None:
                backHead2.random = pointList[nodeRandom[i]]
            else:
                backHead2.random = None
            backHead2 = backHead2.next

        return backHead3.next


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        return
