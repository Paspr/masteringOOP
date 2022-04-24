import pickle, copy
import re


class General(object):
    test = ''
    
    def __init__(self):
        self.test = 'test string'

    def __eq__(self, other): 
        # helper function for compare() method
        if not isinstance(other, General):
            return False
        return self.test == other.test

    def copy(self, source_object, target_object):
        # deepcopy source_object to target_object (both objects exist)
        target_object = copy.deepcopy(source_object)
        return target_object
    
    def clone_object(self, source_object):
        # create new object and clone to it existing source_object
        new_object = General()
        self.copy(new_object, source_object)
    
    def compare(self, first_object, second_object):
        return first_object == second_object
    
    def serialize(self):
        # serialize object
        return pickle.dumps(self)

    def deserialize(self):
        # deserialize object
        return pickle.loads(self)

    def display(self):
        # print object info
        print(self.__dict__)

    def check_type(self, type):
        # return is object an instance of a given type
        return isinstance(self, type)

    def get_real_type(self):
        # prints base class type
        for base in self.__class__.__bases__:
            print(base.__name__)
    
    def assignment_attempt(self, target, source):
        # if source compatible with target assignment is performed
        if self.compare(target, source):
            target=source
        else:
            target = NoneClass().value

class Any(General):
    pass

class NoneClass(Any, General):
    value = ''
    def __init__(self):
        self.value = None


class Vector(General):
    
    def __init__(self, values_list):
        self.storage = values_list
    
    def __len__(self):
        return len(self.storage)

    def add(self, vector):
        if len(self.storage) != len(vector):
            return NoneClass()
        else:
            try:
                return Vector([self.storage[i]+vector.storage[i] for i in range(len(vector))])
            except:
                return NoneClass()


# usage examples

"""
vect = Vector([1,2,3])
vect2 = Vector([1,2,3])
result_vector = vect.add(vect2) # [2, 4, 6]
"""

"""
vect = Vector(['1','2','3'])
vect2 = Vector(['1','2','3'])
result_vector = vect.add(vect2) # ['11', '22', '33']
"""

"""
vect = Vector(['1','2','3'])
vect2 = Vector([1,2,3])
result_vector = vect.add(vect2) # None
"""

"""
vect = Vector([1,2,3])
vect2 = Vector([1,2,3, 4])
result_vector = vect.add(vect2) # None
"""

"""
vect = Vector(Vector(Vector([1,2,3])))
vect2 = Vector(Vector(Vector([1,2,3])))
result_vector = vect.add(vect2) # None
"""