class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    node1 = l1
    node2 = l2
    head = ListNode()
    cur_node = head
    carry_over = 0
    
    while node1 and node2:

        try:
            val1 = node1.val
            node1 = node1.next
        except Exception as e:
            val1 = 0

        try:
            val2 = node1.va2
            node2 = node2.next
        except Exception as e:
            val2 = 0

        _sum = val1 + val2 + carry_over
        mod = (_sum % 10) 
        carry_over = _sum // 10

        new_node = ListNode(mod)
        cur_node.next = new_node
        cur_node = cur_node.next


        if carry_over:
            cur_node.next = ListNode(carry_over)

    return head.next