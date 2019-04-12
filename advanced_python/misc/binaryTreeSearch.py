#!/anaconda/bin/python
"""
This program creates a binary tree, add elements in the tree and display the height of the tree

"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:

    def __init__(self):
        self.height=[]

    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root, height_acc=0):
        #print(root.data, root.left, root.right)
        if not root.left and not root.right :
            print("reached leaf", height_acc)
            self.height.append(height_acc)
            #height_acc = 0

            #return height_acc

        if root.left:

            #height_acc += 1
            print(root.data, "left",root.left.data,height_acc+1)
            self.getHeight(root.left, height_acc+1)
            #height_acc -= 1


        if root.right:
            #height_acc += 1
            print(root.data, "right",root.right.data, height_acc+1)
            self.getHeight(root.right,height_acc+1)

        return max(self.height)

    def PreOrder(self, root):

        res=[]

        if root:
            res.append(root.data)
            res = res + self.PreOrder(root.left)
            res = res + self.PreOrder(root.right)

        return res

    def postOrder(self, root):

        res=[]

        if root:

            res = self.postOrder(root.left)
            res = res + self.postOrder(root.right)
            res.append(root.data)
        return res

    def levelOrder(self, root):

        if root is None:
            return

        queue = []
        l=""
        queue.append(root)
        while len(queue) >0:
            l+=str(queue[0].data)+" "
            temp_node = queue.pop(0)
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)

        print(l)





    def maxDepth(self, root):

        if root is None:
            return 0

        return (self.maxDepth(root.left), self.maxDepth(root.right))

    """
                    3
            2                   5
        1                   4           6
                                                7
    """


    def PrintTree(self, root):
        if root.left:
            root.left.PrintTree()
        print(root.data),
        if root.right:
            root.right.PrintTree()
    # def getHeight(self,root):
    #     #Write your code here
    #     heights=[]
    #     height_pass = 0
    #     while root != None:
    #         if root.left != None:
    #             height_pass += 1
    #             cur = root.left
    #


#T=int(input())
T = 7
myTree = Solution()
root=None
for i in list("3521467"):
    data = int(i)
    root = myTree.insert(root,data)
#height = myTree.getHeight(root)
#myTree.PrintTree(root)
print("Pre order", myTree.PreOrder(root))
print("Post Oder", myTree.postOrder(root))
print("Level Oder", myTree.levelOrder(root))
#print("Max Depth", myTree.maxDepth(root))