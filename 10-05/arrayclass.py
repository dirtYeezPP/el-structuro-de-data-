class ArrayList: 
    def __init__(self, initial_capacity=6):
        self._capacity = initial_capacity
        self._size = 0 
        self._data = [None] * self._capacity
        
    def appendValue(self, value):
        try: 
            empty_index = self._size  
            self._data[empty_index] = value 
            self._size += 1 # the increase mirrors which indices have values already
        except IndexError: 
            print("The list has reached its limit.") # will be replaced later 
    
    def _resize(self, new_capacity):
        pass 
    
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
        try: 
            for j in range(self._size, index, -1): 
                self._data[j] = self._data[j - 1]
            self._data[index] = value 
            self._size += 1 
            print(f"value {value} on index {index}")
        except IndexError:
            print("You cannot do this")
    
    def popValue(self, index=-1):
        try: 
            if self._size == 0: 
                print("arr empty")
                
            if index == -1: 
                index = self._size - 1
            
            pv = self._data[index] 
            for j in range(index, self._size, -1):
                self._data[j] = self._data[j + 1]
            self._data[self._size - 1] = None 
            self._size -= 1 
            print(f"value {pv} popped on index {index}")
        except IndexError: 
            print("index out of range my friendo")        
        
    def removeValue(self, value):
        try: 
            for i in range(self._size): 
                if self._data[i] == value: 
                    for j in range(i, self._size - 1): 
                        self._data[j] = self._data[j+1]
                    self._data[self._size - 1] = None 
                    self._size -= 1 
                    print(f"value {value} removed")
            print("Value not found in the list")
        except: 
            print("nopie dopie")
            
    def __str__(self): 
        return f"{self._data}"
    
a = ArrayList()
a.appendValue(1)
a.appendValue(3)
a.appendValue(6)
a.appendValue(4)
a.appendValue(0)
print(a)

a.appendValue(5)
print(a)

a.popValue()
print(a)
a.popValue(7)

# a.insertValue(0, 43)

# a.insertValue(2, 7)
print(a)

a._resize(7)
print(a)