# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        ans = ListNode(0, head)
        prev = ans
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return ans.next