class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        if head is None:
            #print("adding first Node")
            head = Node(data)
            #print("head => ", head.data, head.next)
        elif head.next is None:
            #print("adding second element to Head")
            head.next = Node(data)
            #print(head)
        else:
            last = head
            #print("Head is not empty", last.data,  last.next)
            while last.next is not None:
              #  print("Pre Last", last.data, last.next)
                last = last.next #return a node which has both data and an pointer
              #  print("Post Last", last.data, last.next)
                # self.display(head)
            last.next = Node(data)

        return head

    def removeDuplicates(self, head):
        print("duplicating linked list")

        if head is None:
           return
        else:
            curr = head
            while curr.next is not None:
                #print(curr.data, curr.next.data)
                if curr.data == curr.next.data:
                    curr.next = curr.next.next
                    #print(curr.data)
                else:
                    #print(curr.data)
                    curr = curr.next

        return head





mylist = Solution()
#T = int(input())
T = list("1222334")
head = None
for i in T:
    #print("Enter new number:")
    data = int(i)
    head = mylist.insert(head, data)
mylist.display(head);
mylist.removeDuplicates(head)

mylist.display(head)