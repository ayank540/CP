from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        self.df = []
    
    # def dfs(self, root):
    #     dfs = deque()
    #     if not root:
    #         return dfs
    #     stack = deque()
    #     stack.appendleft(root)
    #     while len(stack) != 0:
    #         for i in range(len(stack)):
    #             curr = stack.popleft()
    #             dfs.appendleft(curr.data)
    #             if curr.right:
    #                 stack.appendleft(curr.right)
    #             if curr.left:
    #                 stack.appendleft(curr.left)
    #     return dfs

    def dfs(self, root):
        if root:
            self.df.append(root.data)
            self.dfs(root.left)
            self.dfs(root.right)

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
    t.dfs(t.root)
    print(t.df)
    # t.inOrder(t.root)
    # print()
    # res = t.dfs(t.root)
    # print(list(reversed(res)))