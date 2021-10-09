class Queue():
    
    DEQUEUE_NIL = 0 # dequeue() haven't been called
    DEQUEUE_OK = 1 # call of the last dequeue() was successful
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
