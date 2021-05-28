from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def levelOrderTraversal(self, root):
        bfs = []
        if not root:
            return bfs
        q = deque()
        q.append(root)
        while len(q) > 0:
            levelSize = len(q)
            currLevel = []
            for i in range(levelSize):
                curr = q.popleft()
                currLevel.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            bfs.append(currLevel)
        return bfs

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

if __name__=='__main__':
    t = Tree()
    t.root = Node(1)
    t.root.left = Node(2)
    t.root.right = Node(3)
    t.root.left.left = Node(4)
    t.root.left.right = Node(5)
    t.root.right.left = Node(6)
    t.root.right.right = Node(7)
    t.root.left.right.left = Node(8)
    t.inOrder(t.root)
    print()
    res = t.levelOrderTraversal(t.root)
    print(res)