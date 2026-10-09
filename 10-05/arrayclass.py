class ArrayList: 
    def __init__(self, initial_capacity=6):
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
            print("The list has reached its limit.") # will be replaced later 
        
    def getValue(self, index):
        return f" value on index {index} is {self._data[index]}"

    def setValue(self, index, value): 
        self._data[index] = value 
        print(f"value {value} on index {index} set")

    
    def ArrSize(self): 
        return f"amount of elements in list: {self._size}" 
        
    def Arr_is_empty(self):
        return self._size == 0
    
    def insertValue(self, index, value):
        for i in range(self._size): 
            if i == index: 
                for j in range(i, self._size - 1):
                    self._data[j + 1] = self._data[j]
                    # self._data[self._size-1] = self._data[j-1]
                self._data[index] = value 
                self._size += 1
                print("gay")
                return 
        print("No") 
        
    
    def popValue(self, index=-1):
        if self._data[index] != None: 
            self._data[index] = None 
            print(f"Value has been popped on index {index}")
        else: 
            print("there are is no value there to pop my friend")
        
    def removeValue(self, value):
        for i in range(self._size): 
            if self._data[i] == value: 
                for j in range(i, self._size - 1): 
                    self._data[j] = self._data[j+1]
                self._data[self._size - 1] = None 
                self._size -= 1 
                print(f"value {value} removed")
                return 
        print("Value not found in the list")
            
    def __str__(self): 
        # returns string representation of list, i.e [1, 2, 3]
        return f"{self._data}"
    
a = ArrayList()
a.appendValue(1)
a.appendValue(3)
a.appendValue(6)
a.appendValue(4)
a.appendValue(0)
print(a)

a.insertValue(2, 7)
print(a)