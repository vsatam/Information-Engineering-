
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(p, node):
    if p is None:
        p = node
    else:
        if p.val < node.val:
            if p.right is None:
                p.right = node
            else:
                insert(p.right, node)
        else:
            if p.left is None:
                p.left = node
            else:
                insert(p.left, node)


def search(p, key):
    if p is None or p.val == key:
        return p
    if p.val < key:
        return search(p.right, key)
    return search(p.left, key)

def inorder(p):
    if p:
        inorder(p.left)
        print(p.val)
        inorder(p.right)


def minValueNode(node):
    x = node
    while (x.left is not None):
        x = x.left
    return x

def deleteNode(p,key):
    if p is None:
        return p

    if key < p.val:
        p.left = deleteNode(p.left, key)

    elif key > p.val:
        p.right = deleteNode(p.right, key)
    else:
        if p.left is None:
            temp = p.right
            return temp

        elif p.right is None:
            temp = p.left
            return temp
        temp = minValueNode(p.right)
        p.key = temp.key
        p.right = deleteNode(p.right, temp.key)

    return p


r = Node(50)
insert(r, Node(6))
insert(r, Node(21))
insert(r, Node(4))
insert(r, Node(77))
insert(r, Node(82))
insert(r, Node(64))
insert(r, Node(10))
insert(r, Node(34))
insert(r, Node(65))
insert(r, Node(23))
insert(r, Node(76))
insert(r, Node(15))
insert(r, Node(78))
insert(r, Node(89))

print('Original Tree')
inorder(r)
d=search(r,23)
print(d)
print('')
print('Tree after adding the element')
insert(r,Node(51))
inorder(r)
print('')
print('Tree after removing the element')
r=deleteNode(r,23)
inorder(r)
