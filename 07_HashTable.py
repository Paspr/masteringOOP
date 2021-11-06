class HashTable():
    
    PUT_NIL = 0 # put haven't been called
    PUT_OK = 1 # call of the last put() was successful
    PUT_ERROR = 2 # hash table is full
    
    FIND_NIL = 0 # find haven't been called
    FIND_OK = 1 # call of the last find() was successful
    FIND_ERROR = 2 # find() didn't find the value
    
    # constructor
    # postcondition: new hash table is created
    def __init__(self, maxsize):
        self.storage = [None] * maxsize
    
    
    def hash_fun(self, value):
        slot_index = hash(value) % len(self.storage)
        return slot_index
    
    def seek_slot(self, value):
        index = self.hash_fun(value)
        if self.storage[index] is None:
            return index
        else:
            if None in self.storage:
                 return self.storage.index(None)
            else:
                return -1
    
    put_status = PUT_NIL
    
    def put(self, value):
        if self.seek_slot(value) != -1:
            index = self.seek_slot(value)
            self.storage[index] = value
            self.put_status = self.PUT_OK
        else:
            self.put_status = self.PUT_ERROR
            return -1

    find_status = FIND_NIL
        
    def find(self, value):
        index = self.hash_fun(value)
        if self.storage[index] != None and self.storage[index] == value:
            self.find_status = self.FIND_OK
            return index
        else:
            if (value in self.storage):
                self.find_status = self.FIND_OK
                return self.storage.index(value)
            else:
                self.find_status = self.FIND_ERROR
                return -1
        
    # put status request
    def get_put_status(self):
        return self.put_status
    
    # find status request
    def get_find_status(self):
        return self.find_status
    
    # size request
    def size(self):
        return len(self.storage)
