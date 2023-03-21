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


class Solution:
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     cur = head
    #     dum = pre = Node(0)
    #     while cur:
    #         node = Node(cur.val) # 复制节点 cur
    #         pre.next = node # 新链表的 前驱节点 -> 当前节点
    #         # pre.random = '???' # 新链表的 「 前驱节点 -> 当前节点 」 无法确定
    #         cur = cur.next # 遍历下一节点
    #         pre = node
    #     return dum.next

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseLeftWords(s, 2))
