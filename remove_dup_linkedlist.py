# 83. Remove Duplicates from Sorted List
# Easy
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
# Return the linked list sorted as well.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
    	head = ListNode(head)
    	if self.head.val == self.head.next.val:
    		self.head.next = self.head.next.next
    	return self.head

head = [1,1,2]
#Output: [1,2]
sol = Solution()
sol.deleteDuplicates(head)
