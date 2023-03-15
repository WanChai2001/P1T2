class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left == None:
                cur_node.left = node(data)
            else:
                self._insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(data)
            else:
                self._insert(data,cur_node.right)
        elif data == cur_node.data:
            print(" ข้อมูลอยู่ในโครงสร้างแล้ว ")
            return 0

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.data))
            self._print_tree(cur_node.right)

#MAIN
if __name__ == '__main__':
    tree = BST()
    tree.insert(325)
    tree.insert(240)
    tree.insert(240)
    tree.insert(572)
    tree.insert(280)
    tree.insert(280)
    tree.insert(108)
    tree.insert(106)
    tree.insert(106)
    tree.insert(436)
    tree.insert(720)
    tree.insert(730)
    tree.insert(620)
    print(tree.print_tree())
