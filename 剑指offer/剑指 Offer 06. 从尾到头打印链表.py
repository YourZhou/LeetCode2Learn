# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        reverseList = []
        while True:
            if head == None:
                break
            reverseList.append(head.val)
            head = head.next
        reverseList.append(head.val)
        return reverseList[::-1]