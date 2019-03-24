class Node(object):
    def __init__(self):
        self.data = None
        self.next = None


def link_print(head):
    if not head.next:
        return
    cur = head.next
    while cur:
        print(cur.data, end=' ')
        cur = cur.next


def remove_dup(head):
    if head.next is None or head is None:
        return
    outer_cur = head.next
    while outer_cur:
        inner_cur = outer_cur.next
        pre_cur = outer_cur
        while inner_cur:
            if inner_cur.data == outer_cur.data:
                inner_cur = inner_cur.next
                pre_cur.next = inner_cur
            else:
                pre_cur = pre_cur.next
                inner_cur = inner_cur.next
        outer_cur = outer_cur.next


def hash_set(head):
    if head.next is None:
        return
    node_dict = dict()
    cur = head.next
    pre = head
    while cur:
        if cur.data in node_dict:
            cur = cur.next
            pre.next = cur
        else:
            node_dict[cur.data] = None
            pre = pre.next
            cur = cur.next


if __name__ == '__main__':
    head = Node()
    cur = head
    for i in [1, 3, 1, 5, 5, 7]:
        tmp = Node()
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = cur.next

    print('原链表：')
    link_print(head)

    # remove_dup(head)
    hash_set(head)

    print('新链表:')
    link_print(head)
