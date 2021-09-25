class DynArray:
        
    def __init__(self, arraySize = 16):
        self.array = []
        self.count = 0
        self.capacity = 16
        self.peek_status
        self.pop_status
        self.stackSize = arraySize
 

    def makeArray(self, new_capacity):
        if self.count = 0:
            self.array = [None] * new_capacity
            self.capacity = new_capacity
        else:
            temp_array = self.array.copy()
            self.array = temp_array
            self.capacity = new_capacity
            
    
    def getItem(index):
        if ((index >= count) or (index < 0)):
            raise IndexError("index out of range")
        else:
            return self.array[index]
        
    
    def append(item):
        if (self.count + 1 > self.capacity):
            self.makeArray(self.capacity * 2)
            self.array[count] = item
            self.count += 1
        else:
            self.array[count] = item
            self.count += 1
    
    def insert(item, index):
        if index == self.count:
            self.append(item)
            return
        if ((index > self.count) or (index < 0)):
            raise IndexError("index out of range")
        else:
            if (count + 1 > self.capacity):
                self.makeArray(self.capacity * 2)
                self.array_part = self.array[index:]
                temp_array = self.array_part.copy()
                self.array = temp_array
                self.array[index] = item
                self.count += 1
            else:
                self.array_part = self.array[index:]
                temp_array = self.array_part.copy()
                self.array = temp_array
                self.array[index] = item
                self.count += 1
                
                
    def Remove(index):
         if ((index > =self.count) or (index < 0)):
            raise IndexError("index out of range")
        if self.count < (self.capacity / 2):
            if self.count < 16:
                 self.makeArray(16)
            else:
                 self.makeArray(int(self.capacity / 1.5))