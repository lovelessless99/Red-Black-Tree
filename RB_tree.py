from enum import Enum
import math

class color(Enum):
        RED = 0
        BLACK = 1 

def make_comparator(cmp):
        def compare(x, y):
                if cmp(x, y)  : return -1
                elif cmp(y, x): return 1
                else: return 0
        return compare


class comparator:
        
        
        @staticmethod
        @make_comparator
        def greater(num_1, num_2):
                return num_1 > num_2

        
        @staticmethod
        @make_comparator
        def smaller(num_1, num_2):
                return num_1 < num_2


class RB_Node:
        def __init__(self, color: color, key:object, value:object, parent:object) -> None:
                self.parent    = parent
                self.left      = None
                self.right     = None
                self.__color   = color 
                self.__key     = key
                self.__value   = value
        
        def __str__(self):
                return f"Color: {self.__color}, Key: {self.__key}, Value: {self.__value}"

        def set_key(self, key: object):
                self.__key = key

        def set_value(self, value: object):
                self.__value = value

        def set_color(self, color: object):
                self.__color = color

        @property
        def rbnode_color(self)->color:
                return self.__color

        @property
        def rbnode_key(self)->object:
                return self.__key 

        @property
        def rbnode_value(self)->object:
                return self.__value
                



def all_relative(node:RB_Node)->RB_Node:
        return parent_of(parent_of(node)), parent_of(node), left_of(parent_of(parent_of(node))), right_of(parent_of(parent_of(node)))


def parent_of(node:RB_Node)->RB_Node:
        return node.parent if node else None

def left_of(node:RB_Node)->RB_Node:
        return node.left if node else None

def right_of(node:RB_Node)->RB_Node:
        return node.right if node else None

def color_of(node:RB_Node)->RB_Node:
        return node.rbnode_color if node else None


def print_color_str(node :RB_Node)->None:
        # grandpa, parent, l_uncle, r_uncle = all_relative(node)

        if node.rbnode_color == color.BLACK:
                print(f"\033[1;30;40m {str(node)} \033[1;0;40m\n")
                # print(f"爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )
                
        else:
                print(f"\033[1;31;40m {str(node)} \033[1;0;40m\n")
                # print(f"爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )
                
        
class RBTree_Traversal:
        @classmethod
        def max_depth(cls, root: RB_Node)->int:
                if root is None : return 0
                else:
                        left_depth  = RBTree_Traversal.max_depth(root.left)
                        right_depth = RBTree_Traversal.max_depth(root.right)
                        return max(left_depth, right_depth) + 1

        @classmethod
        def levelorder(cls, root: RB_Node)->None:
                depth = RBTree_Traversal.max_depth(root)
                space = " " * (depth << 2)
                output = space

                count = 1
                queue = [root]
                current_level = int(math.log2(count))
                
                while len(queue) > 0:
                        current_node = queue.pop(0)
                        count += 1
                        space = " " * (( depth - current_level ))

                        if current_node is None:  
                                output += f"*{space}"
                        else: 
                                if current_node.rbnode_color == color.BLACK :   
                                        output += f"\033[1;30;40m {str(current_node.rbnode_value)}{space} \033[1;0;40m"
                                else:
                                        output += f"\033[1;31;40m {str(current_node.rbnode_value)}{space} \033[1;0;40m" 
                        
                        queue.append(current_node.left if current_node else None)
                        queue.append(current_node.right if current_node else None)

                        if int(math.log2(count)) > current_level:
                                current_level += 1
                                if not any(queue): break
                                space = " " * (( depth - current_level ) << 2 )
                                output += f"\n{space}"
                print(output)   



        
        @classmethod
        def inorder(cls, root: RB_Node)->None:
                if not root: 
                        print("_")
                        return  
                RBTree_Traversal.inorder(root.left)
                print_color_str(root)
                RBTree_Traversal.inorder(root.right)
                

        @classmethod
        def preorder(cls, root: RB_Node)->None:
                if not root: 
                        print("_")  
                        return
                
                
                print_color_str(root)
                RBTree_Traversal.preorder(root.left)
                RBTree_Traversal.preorder(root.right)

        @classmethod
        def postorder(cls, root: RB_Node)->None:
                if not root: 
                        print("_")  
                        return
                RBTree_Traversal.preorder(root.left)
                RBTree_Traversal.preorder(root.right)
                print_color_str(root)





class RB_Tree:
        def __init__(self):
                self.root = None

        
        ''' left rotate with node p (指標雙向)
        *           pf                      pf
        *          /                       /
        *          p                      pr(r)
        *        /  \                    /  \
        *       pl  pr(r)    ======>    p    rr
        *          /  \                / \
        *          rl  rr             pl rl
        '''
        def __left_rotate(self, p: RB_Node):
                # r, p, pf 都要調整
                if p is not None:
                        r = p.right
                        p.right =  r.left
                        if r.left is not None: 
                                r.left.parent = p
                        r.parent = p.parent

                        if p.parent is None:
                                self.root = r
                        
                        # p is left child of pf
                        elif p.parent.left is p:
                                p.parent.left = r

                        # p is right child of pf
                        elif p.parent.right is p :
                                p.parent.right = r

                        r.left = p
                        p.parent = r


        ''' right rotate with node p (指標雙向)
        *            pf                       pf
        *           /                        /
        *           p                      pl(l)
        *         /   \                    /  \
        *       pl(l)  pr    ======>      ll   p
        *       /  \                          / \
        *      ll  lr                        lr  pr
        '''
        def __right_rotate(self, p: RB_Node):
                
                # l, p, pf 都要調整
                if p is not None:
                        l = p.left
                        p.left =  l.right           # 1
                        if l.right is not None:   
                                l.right.parent = p  # 2
                        l.parent = p.parent         # 3

                        if p.parent is None:
                                self.root = l  
                        
                        # p is left child of pf
                        elif p.parent.left is p:
                                p.parent.left = l   # 4

                        # p is right child of pf
                        elif p.parent.right is p:
                                p.parent.right = l  # 4

                        l.right = p                 # 5
                        p.parent = l                # 6

        '''
        ' # 2-3-4 tree : update element 三種情形
        '   1.  2-3-4  : 新增元素 + 2-節點(節點中有一個元素) = 3 節點 (節點中有兩個元素) 
        '       rbtree : 新增一個紅色節點 + 黑色父親節點 = 上黑下紅 (2個節點) ---> 不用調整
        '
        '   2.  2-3-4  : 新增元素 + 3-節點(節點中有兩個元素) = 3 節點 (節點中有三個元素) 
        '                左3和右3需要調整，兩個左中右不需要調整
        '       rbtree : 新增一個紅色節點 + 上黑下紅 = 排序後中間節點是黑色，兩邊節點都是紅色
        '
        '   3.  2-3-4  : 新增元素 + 4-節點(節點中有四個元素) = 分裂, 中間元素升級為父節點，新增元素和剩下其中一個元素合併
                rbtree : 新增元素 + 爺爺節點, 父節點和叔叔節點都是紅色 = 爺爺節點變紅，父親叔叔變黑，如果爺爺是根節點，再變黑(不影響規則5)
        '
        '''
        def __fix_after_insert(self, x:RB_Node):
                
                # 父節點是黑色就不需要調整，對應情況就是 2, 3
                while x and x is not self.root and x.parent.rbnode_color == color.RED:
                        # x 父節點是爺爺的左子 (左3)
                        
                        grandpa, parent, l_uncle, r_uncle = all_relative(x)

                        if parent is left_of(grandpa):

                                # 第三種情況
                                if r_uncle and r_uncle.rbnode_color == color.RED:
                                        parent.set_color(color.BLACK)
                                        r_uncle.set_color(color.BLACK)
                                        grandpa.set_color(color.RED)

                                        # 改變當前節點繼續比較
                                        x = grandpa

                                # 叔叔節點是黑或是 NULL，右旋，退化成第二種情形
                                else:   
                                        '''
                                               3                3
                                              /                /
                                             2         -->   2.5
                                              \              /
                                               2.5          2
                                        '''

                                        if x is right_of(parent_of(x)):
                                                x = parent_of(x)
                                                self.__left_rotate(x)
                                                # x 已經更新過了 
                                                grandpa, parent, l_uncle, r_uncle = all_relative(x)
                                        
                                                

                                        # 上黑下紅
                                        parent.set_color(color.BLACK)
                                        grandpa.set_color(color.RED)
                                        self.__right_rotate(grandpa) 

                        else:
                                # 第三種情況
                                if l_uncle and l_uncle.rbnode_color == color.RED:
                                        parent.set_color(color.BLACK)
                                        l_uncle.set_color(color.BLACK)
                                        grandpa.set_color(color.RED)
                                        x = grandpa

                                # 叔叔節點是黑或是 NULL，右旋，退化成第二種情形
                                else:   
                                        '''
                                               3                3
                                                \                \
                                                 2         -->   2.5
                                                /                  \
                                              2.5                   2
                                        '''

                                        if x == left_of(parent_of(x)):
                                                x = parent_of(x)        
                                                self.__right_rotate(x)
                                                # x 已經更新過了 
                                                grandpa, parent, l_uncle, r_uncle = all_relative(x)
                                                

                                        # 上黑下紅
                                        parent.set_color(color.BLACK)
                                        grandpa.set_color(color.RED)
                                        self.__left_rotate(grandpa)
                
                self.root.set_color(color.BLACK)


        def insert(self, key:object, value:object):
                
                t = self.root
                if t is None:
                        self.root = RB_Node(color=color.BLACK,key=key,value=value if value else key, parent=None)
                        return

                # 找插入位置
                if key is None: raise ValueError
                
                
                while t:
                        parent = t
                        cmp = comparator.greater(t.rbnode_key, key)
                        if cmp < 0:
                                t = t.left # 沿著左子樹
                        elif cmp > 0:
                                t = t.right  # 沿著右子樹
                        else:
                                t.set_value(value if value else key)
                                return

                
                e = RB_Node(color=color.RED, key=key, value=value if value else key, parent=parent)
               
                # 比較最終落在左子樹，父節點右指針指向 e
                if cmp < 0: 
                        parent.left = e
                else:
                        parent.right = e

                self.__fix_after_insert(e)

               
        # 找到前驅節點
        def __find_predecessor(self, node:RB_Node)->RB_Node:
                if node is None: return None
                elif node.left :
                        p = node.left
                        while p.right:
                                p = p.right
                        return p
                # 右子樹
                else:
                        p = node.parent
                        ch  = node

                        while p and ch == p.left:
                                ch = p 
                                p = p.parent
                        return p


        # 找到後繼節點，大於節點的最小值
        def __find_successor(self, node:RB_Node)->RB_Node:
                if node is None: return None
                elif node.right :
                        
                        p = node.right
                        while p.left:
                                p = p.left
                        return p
                # 左子樹
                else:
                        p = node.parent
                        ch  = node

                        while p and ch is p.right:
                                ch = p 
                                p = p.parent
                        return p


        def get_node(self, key:object)->None:
                if key is None:
                        raise ValueError

                tmp_rbnode = self.root
                while tmp_rbnode:
                        cmp = comparator.greater(tmp_rbnode.rbnode_key, key)
                        if cmp < 0:
                                tmp_rbnode = tmp_rbnode.left # 沿著左子樹
                        elif cmp > 0:
                                tmp_rbnode = tmp_rbnode.right  # 沿著右子樹
                        else:
                                return tmp_rbnode
                return None

        def remove(self, key:object)->None:
                node = self.get_node(key)
                

                if node is None: return None

                old_value = node.rbnode_value
                self.delete_node(node)
                return old_value

        '''
        刪除節點 (like BST)
        1. 刪除葉子節點，直接刪除
        2. 刪除的節點有一個子節點，用子節點覆蓋
        3. 如果刪除的節點有兩個子節點，要找到前驅或後繼節點
        '''
        def delete_node(self, node:RB_Node)->None:
                # print("Remove node:", node)

                # grandpa, parent, l_uncle, r_uncle = all_relative(node)
                # print(f"爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )
                

                ## 3. node has two child
                if node.left and node.right:
                        # print("左右子樹都非空")
                        # successor = self.__find_successor(node)
                        predecessor = self.__find_predecessor(node)
                        
                        # grandpa, parent, l_uncle, r_uncle = all_relative(node)
                        # print(f"Before 爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )
                        # print(f"left child: {left_of(node)}", f"right child: {right_of(node)}")
                        node.set_key(predecessor.rbnode_key)
                        node.set_value(predecessor.rbnode_value)

                        node = predecessor
                        # grandpa, parent, l_uncle, r_uncle = all_relative(node)
                        # print(f"After 爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )
                        # print(f"left child: {left_of(node)}", f"right child: {right_of(node)}")
                        
                # grandpa, parent, l_uncle, r_uncle = all_relative(successor)
                # print(f"爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )

                # grandpa, parent, l_uncle, r_uncle = all_relative(node)
                # print(f"爺爺: {grandpa}, 爸爸: {parent}, 左叔:{l_uncle}, 右叔:{r_uncle}" )

                replace_node = node.left if node.left else node.right
                # print(replace_node)

                ## 2
                if replace_node:
                        # print("只有一顆子樹非空")
                        # 替代者的父親變成原來node的父親
                        replace_node.parent = node.parent
                        # node is root
                        if node.parent is None:
                                self.root = replace_node

                        elif node is node.parent.left:
                                node.parent.left = replace_node
                        
                        elif node is node.parent.right:
                                node.parent.left = replace_node
                        
                        # wait for GC
                        node.left = node.right = node.parent = None

                        # 替換完之後需要調整平衡，替換節點為紅色節點，只要變黑色
                        if node.rbnode_color == color.BLACK:
                                self.fix_after_remove(replace_node)
                                

                # 刪除節點是根節點
                elif node.parent is None:
                        # print("只剩最後一個節點")
                        self.root = None
                
                ## 3 葉子節點 replace_node == None
                else:
                        # print("左右子樹都是空")
                        if node.rbnode_color == color.BLACK:
                                self.fix_after_remove(node)
                                
                        if node.parent:
                                if node is node.parent.left:
                                        node.parent.left = None

                                elif node is node.parent.right:
                                        node.parent.right = None
                                
                                node.parent = None


        def fix_after_remove(self, x: RB_Node)->None:
                # print(x)
                # grandpa, parent, l_uncle, r_uncle = all_relative(x)
                # print("爺爺", grandpa)
                # print("爸爸", parent)
                # print("左叔", l_uncle)
                # print("右叔", r_uncle)

                while x is not self.root and color_of(x) == color.BLACK:

                        if x is left_of(parent_of(x)):
                                r_node = right_of(parent_of(x))
                                
                                # 判斷兄弟節點是否真的是兄弟節點
                                if r_node.rbnode_color == color.RED:
                                        r_node.set_color(color.BLACK)
                                        parent_of(x).set_color(color.RED)
                                        self.__left_rotate(parent_of(x))

                                        # 找到真正的兄弟節點
                                        r_node = right_of(parent_of(x))

                                # 情況三，找兄弟借，兄弟沒得借
                                # print("right brother", r_node)
                                if ( (left_of(r_node) is None and right_of(r_node)  is None) or 
                                       ( left_of(r_node) and left_of(r_node).rbnode_color == color.BLACK and 
                                          right_of(r_node) and right_of(r_node).rbnode_color == color.BLACK) 
                                        ):
                                        r_node.set_color(color.RED)
                                        x = parent_of(x)


                                
                                # 情況二 : 找兄弟借，兄弟不借，找父親借，兄弟代父
                                else: # 分兩種情況，兄弟節點本來是三節點或四節點

                                        # 右孩子為空
                                        if right_of(r_node).rbnode_color == color.BLACK:
                                                left_of(r_node).set_color(color.BLACK)
                                                r_node.set_color(color.RED)
                                                self.__right_rotate(r_node)
                                                r_node = right_of(parent_of(x))
                                        

                                        r_node.set_color(parent_of(x).rbnode_color)
                                        parent_of(x).set_color(color.BLACK)
                                        right_of(r_node).set_color(color.BLACK)
                                        self.__left_rotate(parent_of(x))
                                        x = self.root




                        # x 右孩子
                        else: 
                                l_node = left_of(parent_of(x))
                                
                                # 判斷兄弟節點是否真的是兄弟節點
                                if l_node.rbnode_color == color.RED:
                                        l_node.set_color(color.BLACK)
                                        parent_of(x).set_color(color.RED)
                                        self.__right_rotate(parent_of(x))

                                        # 找到真正的兄弟節點
                                        l_node = left_of(parent_of(x))

                                # print("left brother", l_node)
                                # 情況三，找兄弟借，兄弟沒得借
                                if ( (right_of(l_node) is None and  left_of(l_node) is None) or 
                                     (right_of(l_node) and right_of(l_node).rbnode_color == color.BLACK and 
                                      left_of(l_node)  and left_of(l_node).rbnode_color == color.BLACK) ):
                                        l_node.set_color(color.RED)
                                        x = parent_of(x)
                                        

                                
                                # 情況二 : 找兄弟借，兄弟不借，找父親借，兄弟代父
                                else: # 分兩種情況，兄弟節點本來是三節點或四節點

                                        # 右孩子為空
                                        if left_of(l_node).rbnode_color == color.BLACK:
                                                right_of(l_node).set_color(color.BLACK)
                                                l_node.set_color(color.RED)
                                                self.__left_rotate(l_node)
                                                l_node = left_of(parent_of(x))
                                        

                                        l_node.set_color(parent_of(x).rbnode_color)
                                        parent_of(x).set_color(color.BLACK)
                                        left_of(l_node).set_color(color.BLACK)
                                        self.__right_rotate(parent_of(x))
                                        x = self.root



                # 替代節點是紅色，直接染紅，補償刪除的黑色節點，紅黑數依然保持平衡
                x.set_color(color.BLACK)







if __name__ == "__main__":
        # test_list = [ 1, 5, 3, 2, 4, 8, 9, 7, 0, 6 ]
        test_insert_list = [ i for i in range(1, 11) ]
        test_delete_list = [ 4, 5, 6, 8, 2, 10 ]
        rbt = RB_Tree()

        for i in test_insert_list:
                rbt.insert(i, i) 
        
        # RBTree_Traversal.inorder(rbt.root)

        for i in test_delete_list:
                print(f"================ Before delete {i} ================")
                RBTree_Traversal.levelorder(rbt.root)
                print(f"================ After delete {i} ================")
                rbt.remove(key=i) 
                RBTree_Traversal.levelorder(rbt.root)
                


'''Todo
iterator
Table : code and graph
'''
