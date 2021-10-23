class ParentQueue():
    
    DEQUEUE_NIL = 0 # dequeue() haven't been called
    DEQUEUE_OK = 1 # call of the last dequeue() was succesful
    DEQUEUE_ERROR = 2 # queue is empty
    
    # constructor
    # postcondition: new queue is created
    def __init__(self):
        self.storage = []
    
    # command
    # postcondition: the new item is added to the queue
    def Enqueue(self, item):
        self.storage.append(item)
    
    # initial status of dequeue()
    dequeue_status = DEQUEUE_NIL
    
    # command
    # precondition: queue is not empty
    # postcondition: the last element is deleted
    def Dequeue(self):
        if len(self.storage) != 0:
            result = self.storage.pop(-1)
            self.dequeue_status = self.DEQUEUE_OK
        else:
            result = -1
            self.dequeue_status = self.DEQUEUE_ERROR
        return result
    
    # request    
    def Size(self):
        return len(self.storage)
    
    # status request
    def get_dequeue_status(self):
        return self.dequeue_status


class Queue(ParentQueue):
    pass


class Deque(ParentQueue):
    
    removeFront_OK = 1 # call of the last removeFront() was succesful
    removeFront_ERROR = 2 # queue is empty
    
    # command
    # postcondition: the new item is added to the deque's tail
    def addTail(self, item):
        return super().Enqueue(item)
    
    # command
    # postcondition: the new item is added to the deque's head
    def addFront(self, item):
        self.storage.insert(0, item)
        pass
    
    def removeTail(self):
        return super().Dequeue()
    
    # command
    # precondition: queue is not empty
    # postcondition: the first element is deleted
    def removeFront(self):
        if len(self.storage) != 0:
            result = self.storage.pop(0)
            self.dequeue_status = self.removeFront_OK
        else:
            result = -1
            self.dequeue_status = self.removeFront_ERROR
        return result
