class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nth_elem(head, n):
    dist = 1
    curr_node = head
    nth = None
    while dist < n:
        curr_node = curr_node.next
        dist += 1
    
    nth = head
    while curr.next is not None:
        curr = curr.next
        nth = nth.next
    return nth