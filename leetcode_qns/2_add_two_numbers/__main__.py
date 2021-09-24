# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        sum = 0
        mul = 1
        while num1 or num2:
            if num1:
                sum += num1.val * mul
                num1 = num1.next
            if num2:
                sum += num2.val * mul
                num2 = num2.next
            mul *= 10
        head = ListNode(None)
        tail = None
        for num_str in reversed(str(sum)):
            num = int(num_str)
            if tail:
                tail.next = ListNode(num)
                tail = tail.next
            elif head.val is None:
                head.val = num
            else:
                head.next = ListNode(num)
                tail = head.next
        return head
