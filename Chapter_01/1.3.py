class Node(object):
    def __init__(self):
        self.data = None
        self.next = None


def link_print(head):
    if head is None or head.next is None:
        return
    cur = head.next
    while cur:
        print(cur.data, end=' ')
        cur = cur.next


def add(h1, h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1

    c = 0
    sum = 0
    p1 = h1.next
    p2 = h2.next

    resultHead = Node()
    cur = resultHead
    while p1 and p2:
        tmp = Node()
        sum = c + p1.data + p2.data
        tmp.data = sum % 10
        cur.next = tmp
        cur = cur.next
        c = sum // 10
        p1 = p1.next
        p2 = p2.next
    if p1:
        while p1:
            tmp = Node()
            sum = c + p1.data
            tmp.data = sum % 10
            cur.next = tmp
            cur = cur.next
            c = sum // 10
            p1 = p1.next
    if p2:
        while p2:
            tmp = Node()
            sum = c + p2.data
            tmp.data = sum % 10
            cur.next = tmp
            cur = cur.next
            c = sum // 10
            p2 = p2.next
    if c:
        tmp = Node()
        tmp.data = c
        cur.next = tmp
    return resultHead


if __name__ == '__main__':
    lst1 = [3, 4, 5, 6, 7, 8]
    lst2 = [9, 8, 7, 6, 5]
    h1 = Node()
    cur = h1
    for i in lst1:
        tmp = Node()
        tmp.data = i
        cur.next = tmp
        cur = cur.next

    h2 = Node()
    cur = h2
    for i in lst2:
        tmp = Node()
        tmp.data = i
        cur.next = tmp
        cur = cur.next

    link_print(h1)
    print()
    link_print(h2)
    print()
    result_head = add(h1, h2)
    link_print(result_head)
