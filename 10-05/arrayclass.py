class ArrayList: 
    def __init__(self, initial_capacity=4):
        self._capacity = initial_capacity
        self._size = 0 
        self._data = [None] * self._capacity
    
    def _resize(self, new_capacity):
        # internal method to change size of "array"
        pass 
    
    def appendValue(self, value):
        try: 
            empty_index = self._size  
            self._data[empty_index] = value 
            self._size += 1 # the increase mirrors which indices have values already
        except IndexError: 
            print("The list has reached its limit.")
        
    def getValue(self, index):
        return f" value on index {index} is {self._data[index]}"

    def setValue(self, index, value): 
        self._data[index] = value 

    
    def ArrSize(self): 
        return f"amount of elements in list: {self._size}" 
        
    def Arr_is_empty(self):
        return self._size == 0
    
    def insertValue(self, index, value):
        # inserts element in specific index 
        pass 
    def popValue(self, index=-1):
        # removes and returns an element on specified index 
        pass 
    def removeValue(self, value):
        # takes away first match of "value"
        pass 
    def __str__(self): 
        # returns string representation of list, i.e [1, 2, 3]
        return f"{self._data}"
    
a = ArrayList()
a.appendValue(4)
a.appendValue(5)
a.appendValue(3)
a.appendValue(4)
print(a)
# a.appendValue(7) -> list reached limit yippie works 

a.setValue(0, 9)

print(a.ArrSize())
print(a.getValue(0))
print(a)
print(a.Arr_is_empty())