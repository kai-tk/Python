#ノードの定義
class Node:
    def __init__(self,data,parent,left,right,count):
        self.data=data
        self.parent=parent
        self.left=left
        self.right=right
        self.count=count

#ダミーノード
def NullNode(parent=None):
    return Node(None,parent,None,None,0)

#二分探索木の定義
class BST:
    #初期化
    def __init__(self):
        self.root=NullNode(None)
        self.root.right=NullNode(self.root)
        self.root.left=NullNode(self.root)
        self.root.count=1

    #挿入(insert(data)でdataを挿入,insert(data,True)で回転)
    def insert(self,data,rot=False):
        self.root=self._insert(data,None,self.root,0,rot)

    def _insert(self,data,parent,cur_node,direction,rot):
        if cur_node.data is None:
            if cur_node.parent is None:
                self.root.data=data
            else:
                cur_node=Node(data,parent,NullNode(cur_node),NullNode(cur_node),1)
                if direction==1:
                    cur_node.parent.left=cur_node
                elif direction==2:
                    cur_node.parent.right=cur_node
        elif data<cur_node.data:
            cur_node.count+=1
            cur_node.left=self._insert(data,cur_node,cur_node.left,1,rot)
            if rot:
                cur_node=self.rotR(cur_node)
        elif data>cur_node.data:
            cur_node.count+=1
            cur_node.right=self._insert(data,cur_node,cur_node.right,2,rot)
            if rot:
                cur_node=self.rotL(cur_node)
        elif data==cur_node.data:
            tempNode=cur_node
            while tempNode.parent:
                tempNode=tempNode.parent
                tempNode.count-=1
        return cur_node

    #列挙(show()で全dataを表示)
    def show(self):
        self._show(self.root,0)

    def _show(self,cur_node,depth):
        if cur_node.data!=None:
            self._show(cur_node.right,depth+1)
            for i in range(depth):
                print("\t",end="")
            print(cur_node.data,cur_node.count)
            self._show(cur_node.left,depth+1)

    #要素数(count()で要素数を返す)
    def count(self):
        return self.root.count

    #探索(find(data)でdataが存在するときTrue)
    """無回転時のみ"""
    def find(self,data):
        if self.root.data is None:
            return None
        cur_node=self.root
        while cur_node.data:
            if data==cur_node.data:
                return True
            elif data<cur_node.data:
                cur_node=cur_node.left
            else:
                cur_node=cur_node.right
            return False

    #回転
    def rotR(self,cur_node):
        tempNode=cur_node.left
        cur_node.left=tempNode.right
        tempNode.right.parent=cur_node
        tempNode.right=cur_node
        tempNode.parent=cur_node.parent
        cur_node.parent=tempNode
        tempNode.count=cur_node.count
        cur_node.count=tempNode.count-tempNode.left.count-1
        return tempNode

    def rotL(self,cur_node):
        tempNode=cur_node.right
        cur_node.right=tempNode.left
        tempNode.left.parent=cur_node
        tempNode.left=cur_node
        tempNode.parent=cur_node.parent
        cur_node.parent=tempNode
        tempNode.count=cur_node.count
        cur_node.count=tempNode.count-tempNode.right.count-1
        return tempNode


Tree=BST()
while True:
    n=int(input())
    if n==0:
        break
    Tree.insert(n,True)
    print("ShowStart")
    Tree.show()
    print("ShowEnd")
