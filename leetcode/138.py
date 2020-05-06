"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pos = head
        while pos:
            node = Node(pos.val, pos.next, None)
            pos.next = node
            pos = node.next
        pos = head
        dummy = Node(0)
        tail = dummy
        while pos:
            newnode = pos.next
            newnode.random = pos.random.next if pos.random else None
            pos = newnode.next
            tail.next = newnode
            tail = newnode
        return dummy.next
            
