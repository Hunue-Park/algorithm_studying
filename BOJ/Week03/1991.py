class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

def preorder(node):
    # Root
    print(node.item, end='')    
    # Left
    if node.left != '.':
        preorder(tree[node.left])
    # Right
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        inorder(tree[node.right])
    
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end='')

if __name__ == "__main__":

    N = int(input())
    # dictionary type for tree structure.
    tree = {}
    # input values.
    for _ in range(N):
        node, left, right = map(str, input().split())
        tree[node] = Node(item=node, left=left, right=right)
    # root 인 A 값을 집어넣음으로 순회 시작.
    preorder(tree['A'])
    # 이 print() 는 공백, 줄바꿈을 위함. 
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])
    
