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
        l1Cursor = l1
        l2Cursor = l2
        if l1Cursor == None and l2Cursor == None:
            return None

        if l1Cursor == None:
            return l2Cursor
        if l2Cursor == None:
            return l1Cursor
        retNode = None
        listNode = []
        while l1Cursor != None:
            listNode.append(l1Cursor)
            l1Cursor = l1Cursor.next
        while l2Cursor != None:
            listNode.append(l2Cursor)
            l2Cursor = l2Cursor.next

        listNode = sorted(listNode, key=lambda listnode: listnode.val)
        print(listNode)

        retNode = listNode[0]
        index = 1
        retNodeCursor = retNode
        while index < len(listNode):
            retNodeCursor.next = listNode[index]
            retNodeCursor = retNodeCursor.next
            index += 1
        return retNode


def playNode(nodes):
    while nodes != None:
        print(nodes.val)
        nodes = nodes.next


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

# playNode(l1_node1)
# playNode(l2_node1)

sol = Solution()
retnode = sol.mergeTwoLists(l1_node1, l2_node1)
playNode(retnode)
