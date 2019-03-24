class LNode(object):
    def __init__(self):
        self.data = None
        self.next = None


def reverse(head):
    pre = next = None
    cur = head.next
    while cur:
        next = cur.next
        cur.next = pre
        # 节点后移
        pre = cur
        cur = next
    head.next = pre
    return head


def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    else:
        new_head = recursive_reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head


def recursive_reverse_start(head):
    if head is None:
        return
    firstNode = head.next
    new_head = recursive_reverse(firstNode)
    head = LNode()
    head.next = new_head
    return head


def insert_reverse(head):
    if head.next is None or head is None:
        return
    cur = head.next.next
    head.next.next = None
    while cur:
        next = cur.next
        cur.next = head.next
        head.next = cur
        cur = next
    return head


def print_link(head):
    cur = head.next
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print('\n')


def print_reverse(firstNode):
    if firstNode is None:
        return
    print_reverse(firstNode.next)
    print(firstNode.data, end=' ')


if __name__ == '__main__':
    i = 1
    head = LNode()

    cur = head

    for i in range(10):
        tmp = LNode()
        tmp.data = i
        cur.next = tmp
        cur = tmp

    cur = head.next

    print('逆序前:')
    print_link(head)

    # head = reverse(head)
    # head = recursive_reverse_start(head)
    # head = insert_reverse(head)
    print('逆序后')
    print_link(head)
    print_reverse(head.next)
