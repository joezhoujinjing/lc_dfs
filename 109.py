class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        root = TreeNode(head.val)
        return root



tmp=ListNode(1)
head = tmp
for i in range(2,10):
    tmp.next=ListNode(i)
    tmp=tmp.next

slow=head
fast=head
while fast.next!=None and fast.next.next!=None:
    slow=slow.next
    fast=fast.next.next
print slow.val
print slow.next.val
print head.val
sl=Solution()
#print sl.sortedListToBST(head)
