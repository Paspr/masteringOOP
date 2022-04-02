import pickle, copy


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

class Any(General):
    pass