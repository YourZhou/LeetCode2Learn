class SingleNode(object):
    def __init__(self,item):
        self.item = item
        self.next = None

"""单链表数据结构类，具有以下功能"""
class SingleLinkList(object):
    def __init__(self):
        """存放一个头节点head，好用来指向第一个节点"""
        self._head = None # _ 私有属性,head=None说明P指向的单链表中没有node

    def isEmpty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # current游标用来遍历节点，初始时指向头节点
        cur = self._head
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item,end=" ")
            cur = cur.next

    def add(self,item):
        """头部添加元素"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self,item):
        """尾部添加元素"""
        node = SingleNode(item)
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node



if __name__ == '__main__':
    li = SingleLinkList()
    print(li.isEmpty())
    print(li.length())
    node = SingleNode(3)
    li.append(11111)
    li.append(11112)
    li.append(11113)
    li.append(11114)
    li.append(11112)
    li.append(11116)
    li.append(11117)
    print(li.length())
    li.travel()