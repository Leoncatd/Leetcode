# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        strl1 = ''
        strl2 = ''
        while l1:
            strl1 = strl1 + str(l1.val)
            l1 = l1.next
        strl1 = int(strl1)

        while l2:
            strl2 = strl2 + str(l2.val)
            l2 = l2.next
        strl2 = int(strl2)
        summ = list(str(strl1 + strl2))

        res = ListNode(0)
        head = res
        for i in summ:
            res.next = ListNode(int(i))
            res = res.next

        return head.next
