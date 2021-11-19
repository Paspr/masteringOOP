class NativeDictionary():
    
    PUT_NIL = 0 # put haven't been called
    PUT_OK = 1 # call of the last put() was succesful
    
    GET_NIL = 0 # get haven't been called
    GET_OK = 1 # call of the last get() was succesful
    GET_ERROR = 2 # get() didn't find the value
    
    REMOVE_NIL = 0 # remove haven't been called
    REMOVE_OK = 1 # call of the last remove() was succesful
    REMOVE_ERROR = 2 # remove() didn't find the value
    
    # constructor
    # postcondition: new NativeDictionary is created
    def __init__(self):
        self.storage = [[]]

    def is_key(self, key):
        hash_key = hash(key) % len(self.storage)
        key_exists = False
        slot = self.storage[hash_key]	
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True 
                return key_exists
        return -1    
    
    put_status = PUT_NIL
    
    def put(self, key, value):
        hash_key = hash(key) % len(self.storage)
        key_exists = False
        slot = self.storage[hash_key]	
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True 
                break
        if key_exists:
            slot[i] = (key, value)
            self.put_status = self.PUT_OK
        else:
            slot.append((key, value))
            self.put_status = self.PUT_OK
    
    get_status = GET_NIL
    
    def get(self, key):
        hash_key = hash(key) % len(self.storage)
        slot = self.storage[hash_key]	
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                self.get_status = self.GET_OK
                return v
        self.get_status = self.GET_ERROR
        return -1    
    
    remove_status = REMOVE_NIL
    
    def remove(self, key):
        hash_key = hash(key) % len(self.storage)
        key_exists = False
        slot = self.storage[hash_key]	
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True 
                break
        if key_exists:
            del slot[i]
            self.remove_status = self.REMOVE_OK
        else:
            self.remove_status = self.REMOVE_ERROR
         
    
    # put status request
    def get_put_status(self):
        return self.put_status
    
    # get status request
    def get_get_status(self):
        return self.get_status
    
     # remove status request
    def get_remove_status(self):
        return self.remove_status
    
    # size request
    def size(self):
        return sum([len(listElem) for listElem in self.storage])