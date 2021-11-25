# binary search tree
import sys
input = sys.stdin.readline

# 노드 생성과 삽입
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(Node):
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)
    
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

if __name__ == "__main__":
    root = Node(int(input()))
    bst = BinarySearchTree(root)
    while True:
        try:
            bst._insert_value(int(input()))
        except:
            break