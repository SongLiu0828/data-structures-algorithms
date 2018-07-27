class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)
        #添加到deque的首部

    def addRear(self, item):
        self.items.insert(0, item)
        #添加到deque的尾部

    def removeFront(self):
        return self.items.pop()
        #从deque中删除首项

    def removeRear(self):
        return self.items.pop(0)
        #从deque中删除尾项

    def size(self):
        return len(slef.items)
        #返回项数
