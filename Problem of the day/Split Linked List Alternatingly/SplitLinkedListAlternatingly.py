class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        if not head:
            return [None, None]

        head1, head2 = None, None
        current1, current2 = None, None

        flag = True
        current = head

        while current:
            if flag:
                if not head1:
                    head1 = current1 = Node(current.data)
                else:
                    current1.next = Node(current.data)
                    current1 = current1.next
            else:
                if not head2:
                    head2 = current2 = Node(current.data)
                else:
                    current2.next = Node(current.data)
                    current2 = current2.next

            flag = not flag
            current = current.next

        return [head1, head2]

def printList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = Node(0)
head.next = Node(1)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = Node(1)

solution = Solution()
lists = solution.alternatingSplitList(head)