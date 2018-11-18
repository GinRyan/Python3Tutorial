"""将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 
      1->3->4
输出：1->1->2->3->4->4

1->5->9
7->16->17->20

1->
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retLink = None
        retCursor = None
        l1Cursor = l1
        l2Cursor = l2
        while True:
            if l1Cursor.val < l2Cursor.val:#当前节点小值为胜，当前节点前移
                if retLint == None:#当结果节点为空的时候，设定当前胜利节点为结果节点，结果节点前移
                    retLint = l1Cursor
                    retCursor = retLint
                else :
                    retCursor.next = l1Cursor
                l1Cursor = l1Cursor.next
            elif l1Cursor.val > l2Cursor.val:
                pass
            break
        return retLink


l1_node1 = ListNode(1)
l1_node2 = ListNode(2)
l1_node3 = ListNode(8)

l1_node1.next = l1_node2
l1_node2.next = l1_node3

l2_node1 = ListNode(5)
l2_node2 = ListNode(13)
l2_node3 = ListNode(16)

l2_node1.next = l2_node2
l2_node2.next = l2_node3

sol = Solution()
retnode = sol.mergeTwoLists(l1_node1, l2_node1)
print(retnode)
while retnode != None:
    print(retnode.val)
    retnode = retnode.next
