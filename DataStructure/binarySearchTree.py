class TreeNode:
    def __init__(self, item, left, right):
        self.item = item 
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, x) -> TreeNode:
        return self.__searchItem(self, x)
    
    def __searchItem(self, tNode:TreeNode , x):
        if tNode == None:
            return None
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.searchItem(tNode.left, x)
        else:
            return self.searchItem(tNode.right, x)

    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
        if tNode is None:
            tNode = TreeNode(newItem, None, None)
        elif newItem < tNode.item:
            tNode.left = self.insertItem(tNode.left, newItem)
        else:
            tNode.right = self.insertItem(tNode.right, newItem)
        return tNode

    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
        if tNode is None:
            return None
        elif x is tNode.item:
            tNode = self.__deleteItem(tNode)
        elif x < tNode.item:
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode
    
    def __deleteNode(self, tNode:TreeNode) -> TreeNode:
        if tNode.left is None and tNode.right is None:
            return None
        elif tNode.left is None:
            return tNode.right
        elif tNode.right is None:
            return tNode.left
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode

    def isEmpty(self) -> bool:
        return self.__root is self.NIL

    def clear(self):
        self.__root = self.NIL

    def print_tree(self):
        pass

bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(7550)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.delete(7550)
bst1.delete(10)
bst1.print_tree()
