from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=' ')
            self.inOrder(root.right)

    def bfs(self, root):
        bfs = []
        if not root:
            return bfs
        q = deque()
        q.append(root)
        while len(q) != 0:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                bfs.append(curr.data)
        return bfs

    def levelOrderSuccessor(self, root, key):
        if not root:
            return Node(-1)
        q = deque()
        q.append(root)
        while len(q) != 0:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            if curr.data == key:
                break
        if len(q):
            return q.popleft()
        else:
            return Node(-1)


if __name__ == '__main__':
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
    print(t.bfs(t.root))
    res = t.levelOrderSuccessor(t.root, int(input())).data
    print(res)
