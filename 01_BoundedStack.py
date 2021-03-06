class BoundedStack:
        
    def __init__(self, stackSize = 32):
        self.stack = [None] * stackSize
        self.peek_status
        self.pop_status
        self.stackSize = stackSize
   
    POP_NIL = 0 # pop haven't been called yet
    POP_OK = 1 # pop was successful
    POP_ERR = 2 # pop was not successful
    PEEK_NIL = 0 # peek haven't been called yet
    PEEK_OK = 1 # peek was successful
    PEEK_ERR = 2 # peek was not successful
    PUSH_NIL = 0 # push haven't been called yet
    PUSH_OK = 1 # push was successful
    PUSH_ERR = 2 # push was not successful
    
    def clear(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def BoundedStack(self):
       self.clear()
   
    push_status =  PUSH_NIL
    
    def push(self, value):
        if None in self.stack:
            freeIndex = self.stack.index(None)
            self.stack.insert(freeIndex, value) 
            self.push_status = self.PUSH_OK
            self.pop()
        else:
            self.push_status = self.PUSH_ERR
   
    peek_status = PEEK_NIL
    pop_status = POP_NIL
    
    def pop(self):
        if self.size() > 0:
           return self.stack[-1]
           self.pop_status = self.POP_OK
        else:
           self.pop_status = self.POP_ERR
   
    def peek(self):
        if self.size() > 0:
            result = self.stack[-1]
            self.peek_status = self.PEEK_OK
        else:
            result = 0
            self.peek_status = self.PEEK_ERR
        return result 

   
    def get_pop_status(self):
       return self.pop_status
   
    def get_peek_status(self):
       return self.peek_status
   
    def get_push_status(self):
       return self.push_status
