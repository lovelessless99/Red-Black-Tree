# 紅黑樹
> * [課程網頁](https://www.bilibili.com/video/BV135411h7wJ/?p=4&spm_id_from=pageDriver)
> * [说点不一样的树](https://www.jianshu.com/p/9290529e3725)
> * [我画了近百张图来理解红黑树.md](https://github.com/JasonGaoH/KnowledgeSummary/blob/master/Docs/Java/%E6%88%91%E7%94%BB%E4%BA%86%E8%BF%91%E7%99%BE%E5%BC%A0%E5%9B%BE%E6%9D%A5%E7%90%86%E8%A7%A3%E7%BA%A2%E9%BB%91%E6%A0%91.md)
> * [TreeSet and TreeMap](https://github.com/CarpenterLee/JCFInternals/blob/master/markdown/5-TreeSet%20and%20TreeMap.md)

## 1. 二分搜尋樹
1. 遞迴定義 : 節點比左子樹都大，比右子樹都小
2. 高度決定搜尋效率
3. 不適合用已排序的資料，退化成linked list，複雜度為O(n)

4. 和紅黑樹同是二元搜尋樹，搜尋值的方式也一樣( >Value 往右找，< Value 往左找 )

5. Traversal (和紅黑樹同)
    * Inorder  (left->root->right)(較常用)
    * Preorder (root->left->right)
    * Postorder(left->right->root)

Ex:
```
       4
     /  \
    2    6
  /  \  / \
 1   3 5   7

* Preorder   :  4 213 657
* Inorder  :  123 4 567
* Postorder :  132 576 4 
```

6. FindMin : 沿著左子樹走到底
7. FindMax : 沿著右子樹走到底
8. FindPredecessor :  小於當前節點的最大值
9. FindSuccssor : 大於當前節點的最小值
10. Delete : 找前驅節點或後繼節點來替代
    * 葉節點直接刪除
    * 只有一個子節點直接拿來替代 (本質上就是找前驅或後繼節點)
    * 有兩個子節點的，需要找到替代節點 (前驅或後繼節點，都可以)
    * **和紅黑樹相同，只是因為刪除可能會破壞紅黑數的平衡，所以多了著色、旋轉過程** 
  

## 2. 簡介 - 高等平衡樹 
1. BST 缺點 : 退化問題 (solve AVL Tree) 
2. 具所有 BST 的特性
3. 兩種最具代表的自平衡樹
    * AVL Tree
    * RB Tree  


### 2-1. AVL Tree
精神: 樹的高度不超過 1 (旋轉後續會仔細提到)

Ex : insert 10, 9, 8, 7, 6, 5 ,4, 3, 2, 1，共六次旋轉

insert 8 (10不平衡)
```
    10                   9
   /                   /   \
  9      ---------->  8    10
 /       (R-rotate)
8

```

insert 7 
```
       9
     /   \
    8    10
  /
 7
```
insert 6 (8, 9 不平衡)
```
         9                              9
       /   \                           /  \ 
      8     10                       7    10
    /           ---------------->   / \
   7             (R-rotate to 8)   6   8
  /
 6
```

insert 5 (9 不平衡)
```
        9                             7
      /  \                           /  \
     7    10    ---------------->   6    9
    / \           (R-rotate to 9)  /    /  \
   6   9                          5    8   10
  /
 5
```

insert 4 (6 不平衡)
```
            7                                7
          /  \                             /  \
         6    9      ---------------->    5    9
        /    / \      (R-rotate to 6)    / \   / \
      5     8   10                      4  6  8  10
     /
    4
```

insert 3
```
            7  
          /   \            
         5     9
        / \   /  \
      4   6  8   10
     /
    3
```

insert 2 (4, 5 不平衡)
```
            7                                    7
          /   \                                /  \
         5     9                              5     9
        / \   / \                            / \   / \
      4  6   8   10   ---------------->     3  6  8  10
     /                 (R-rotate to 4)     / \
    3                                     2  4
   /
  2
```

insert 1 (5 不平衡)
```
         7                                     7
        /  \                                 /   \
      5     9                               3     9
     / \   / \                             / \    / \
    3  6  8  10    ---------------->      2  5   8  10
   / \              (R-rotate to 5)      /  / \ 
  2  4                                  1  4   6
 /
1
```
### 2-2. Red Black Tree
1. 黑色節點平衡(每條path的黑色節點數量相同)，但是有可能不是AVL樹
以下圖為例，是紅黑樹但不是AVL樹，所以紅黑樹的性質是介於BST和AVL之間的，AVL Tree 相對來說條件太嚴格了😅😅
![](https://i.imgur.com/zPJxPVJ.png)

2. AVL 樹實現較複雜，且插入跟刪除性能較紅黑樹差，實際應用紅黑樹較廣泛
3. Ex : Java HashMap, TreeSet，Java 8 因為把 Hashmap 用紅黑樹取代Linked list，性能提升不少
4. 來自 **2-3-4 樹** 

### 2-3. 2-3-4 Tree
1. 所有葉節點有相同深度
2. 節點只能有 2-節點, 3-節點, 4-節點
    * 2-節點 : 包含 1 個元素的節點，有 2 個子節點
    * 3-節點 : 包含 2 個元素的節點，有 3 個子節點
    * 4-節點 : 包含 3 個元素的節點，有 4 個子節點 

3. 所有節點至少有一個元素
4. 一定要是 Full complete tree (葉子全滿，且存在)
5. RB tree 的起源，查詢如普通的BST，但是節點元素個數不確定，可能需要其他資料結構儲存或表示，所以不易實現。

6. 位置滿了讓中間的數字升一層，如同Ｂ-Tree之類的多路查詢樹
7. **一個 2-3-4 tree 對應多個紅黑數，但一個紅黑樹只能對應一個2-3-4 樹** 
![](https://i.imgur.com/70lg0ml.png)

## 3. Red Black Tree 和 2-3-4 樹的等價關係 (核心重點，以此為基礎逆推紅黑樹)

* 紅黑數新增的一定是紅色的
* 2-3-4 Tree 可轉成多個紅黑樹，但一個紅黑樹只能轉成一種 2-3-4 Tree

* 2-節點 : 黑色
* 3-節點 : 上黑下紅 (左頃或右頃) --> 可以有兩種型態，造就對應多種紅黑樹的情形
* 4-節點 : 紅黑紅 (上黑下紅，中間黑且下面兩個紅)
* 裂變   : 看圖例 (如果裂變是根節點，則再次轉為黑色，中間升層變紅色，下面兩個變黑色，進來的紅色看值靠近)

    
左 : 2-3-4 樹，右 : RB Tree
![](https://i.imgur.com/7YOPW0u.png)
![](https://i.imgur.com/nc3hQhj.png)
 
![](https://i.imgur.com/PRu0FcN.png)

Ex: 
原 2-3-4 樹

![](https://i.imgur.com/bDqSl4O.png)

紅黑樹轉換第(1)種  
![](https://i.imgur.com/LMdU2wU.png)

紅黑樹轉換(2)
![](https://i.imgur.com/uFauKdL.png)

可以觀察出 
* 每條從根走到葉的的路徑黑節點樹相同
* 紅色節點不會單獨存在，一定和紅節點上面的黑色節點是一個整體


紅黑樹 + 新增節點(紅色) = 對等 2-3-4 樹新增一個節點
![](https://i.imgur.com/fmzNJlg.png)


## 4. Red Black Tree
### 五大性質
* 節點是紅或是黑
* 根是黑色
* 所有葉子都是黑色(葉子是NULL節點)
* 每個紅色節點必須有兩個黑色子節點，且根到葉子的路徑上不可以有兩個連續的紅色節點
* 任一個節點到每個葉子的所有簡單路徑都包含相同數目的黑色節點 (黑色平衡)

### 逆推性質
* 節點是紅或是黑 ===> 甭推
* 根是黑色
    * 情況一 : 2-3-4 樹是 2 節點
    ![](https://i.imgur.com/dfbKuZW.png)


    * 情況二 : 2-3-4 樹是 3 節點
    ![](https://i.imgur.com/DTUg9LO.png)
    ![](https://i.imgur.com/nEFUsfa.png)


    * 情況三 : 2-3-4 樹是 4 節點(也是上黑下紅)

* 所有葉子都是黑色(葉子是NULL節點) ===> 甭推
* 不可以有兩個連續的紅色節點
    * 原始紅黑樹
    ![](https://i.imgur.com/udCjW6j.png)
    * 逆推 2-3-4 樹
    ![](https://i.imgur.com/UU9yfeu.png)
     因為只能掛三種節點，子樹一定是黑根

* 任一個節點到每個葉子的所有簡單路徑都包含相同數目的黑色節點 (黑色平衡)

    * 2-3-4 樹葉子高度都相等(Full Complete Tree)，且每個節點轉乘紅黑樹後必有一個黑色，所以即可得此性質，簡單吧



### 右、左旋
[參考連結](https://xuezhaokun.github.io/150-algorithm/)
![](https://upload.wikimedia.org/wikipedia/commons/3/31/Tree_rotation_animation_250x250.gif)
![](https://codertw.com/wp-content/uploads/img/2z30o8Fo81.jpg)
![](https://raw.githubusercontent.com/JasonGaoH/Images/master/red_black_tree_rotate_right.gif)

### 2-3-4 樹新增節點對比紅黑樹的新增節點 (Insertion)

2-3-4 樹新增節點 全部在葉節點完成
![](https://i.imgur.com/guFbWXN.png)

第一步因為只有一個根節點，所以由紅轉黑
![](https://i.imgur.com/UC3UF5k.png)

變3節點
![](https://i.imgur.com/W5zggZn.png)

變4節點，紅黑樹有四種情況
![](https://i.imgur.com/Vy8YjW8.png) 
![](https://i.imgur.com/iC2UjWM.png)

再新增一個節點，分裂也四種情形
![](https://i.imgur.com/tkn37W3.png)
![](https://i.imgur.com/dkJhIC9.png)


### 2-3-4 樹新增節點對比紅黑樹的刪除節點 
一般二元搜尋樹的刪除
![](https://i.imgur.com/gg1j481.png)
Ex : 刪掉 5，只能用 4 或 6 替代，但一般不會直接刪掉，而是取代值。例如把 5 改成 4，再把 4 刪除就好了，相當於刪除葉節點，只是如果是物件拷貝太複雜的的話不太適用

刪除方案 : 
1. 刪除葉子節點，直接刪除
2. 刪除的節點有一個子節點，用子節點覆蓋
3. 如果刪除的節點有兩個子節點，要找到前驅或後繼節點

    1. 找到前驅節點，複製前驅節點的值直接覆蓋到準備被刪除的節點的值，然後刪除前驅節點
    2. 找到後繼節點，複製後繼節點的值直接覆蓋到準備被刪除的節點的值，然後刪除後繼節點
    3. 被刪除的前驅或後繼只有兩種情況
        * 被刪節點是葉子節點
        * 被刪節點只有一個子節點

對等關係
> * 注意，因為紅黑樹是由 2-3-4樹 轉換的，2-3-4樹每個節點至少都是 2 節點，所以左右節點一定存在，和二分搜尋樹不同
> * 紅黑樹倒數兩層為 2-3-4 樹的葉子節點 
> * 紅黑樹上面的刪除節點一定是2-3-4樹上面的葉子節點，因為如上一小段所述，刪除節點由前驅或後繼節點替代，而前驅、後繼正好就是紅黑數或是2-3-4樹的葉子節點

![](https://i.imgur.com/nf67Rir.png)
1. 自己能搞定(最簡單) : 2-3-4 樹 3,4 節點刪除一個節點合法
              對應葉子節點是3節點或是 4 節點
              所以紅色節點刪掉不用調整
            
![](https://i.imgur.com/QmGdaUQ.png)


2. 自己不能搞定(沒小孩) : Ex: 刪除 5 or 3，刪了就非法。要跟兄弟借，但是兄弟不借，父親下來幫忙，兄弟找一人去替代父親



找真正兄弟
![](https://i.imgur.com/iWQJPiq.png)
在2-3-4樹，5的兄弟是(6.5, 7)，但是在紅黑樹上，卻是8，因此要做一些操作，把2-3-4 上 6, 8 顏色換掉，對應的紅黑樹就會是兄弟節點了
![](https://i.imgur.com/O2shqhn.png)


四節點的情形:
1. 第一種情況 : 2-3-4借一個節點，紅黑樹要旋轉兩次
1. 第二種情況 : 2-3-4兩個節點，紅黑樹要旋轉一次



3. 找兄弟借，兄弟沒得借(情同手足，再自損)


## 5.比較
[參考連結](https://www.jianshu.com/p/9290529e3725)
![](https://upload-images.jianshu.io/upload_images/4843688-261e8633aa371113.png?imageMogr2/auto-orient/strip|imageView2/2/w/937/format/webp)

