class HashTable():
    
    PUT_NIL = 0 # put haven't been called
    PUT_OK = 1 # call of the last put() was successful
    PUT_ERROR = 2 # hashtable is full
    
    FIND_NIL = 0 # find haven't been called
    FIND_OK = 1 # call of the last find() was successful
    FIND_ERROR = 2 # find() didn't find the value
    
    # constructor
    # postcondition: new hashtable is created
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
    

class PowerSet(HashTable):
      
    REMOVE_NIL = 0 # remove haven't been called yet
    REMOVE_OK = 1 # call of the last remove() was successful
    REMOVE_ERROR = 2 # remove() didn't remove the value
    
    def put(self, value):
          if value not in self.storage:
              if self.seek_slot(value) != -1:
                  index = self.seek_slot(value)
                  self.storage[index] = value
                  self.put_status = self.PUT_OK
              else:
                self.put_status = self.PUT_ERROR
                return -1
          else:
              self.put_status = self.PUT_ERROR
              return -1
      
    remove_status = REMOVE_NIL
      
    def remove(self, value):
          if value in self.storage:
              index = self.storage.index(value)
              self.storage[index] = None
              self.remove_status = self.REMOVE_OK
          else:
               self.remove_status = self.REMOVE_ERROR
    
    def intersection(self, second_set):
        if len(self.storage) >= len(second_set.storage):
            result_set = PowerSet(len(second_set.storage))
        else:
            result_set = PowerSet(len(self.storage))
        for x in self.storage:
            if x in second_set.storage:
                result_set.put(x)
        return result_set
   
    def union(self, second_set):
        result_set = PowerSet(len(self.storage) + len(second_set.storage))
        for i in self.storage:
            result_set.put(i)
        for i in second_set.storage:
            result_set.put(i)
        return result_set    
    
    def difference(self, second_set):
        result_set = PowerSet(len(self.storage))
        for i in self.storage:
            if i not in second_set.storage:
                result_set.put(i)
        return result_set    

    
    def issubset(self, second_set):
        issubset = True
        for i in second_set.storage:
            if i not in self.storage:
                issubset = False 
        return issubset     

    # remove status request
    def get_remove_status(self):
        return self.remove_status
