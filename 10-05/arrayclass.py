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
        # inserts element in specific index 
        # 1. skapa en ny större array - om arrayen är full 
        # 2. loopa igenom men byt värdet av det angivna indexet 
        # 3. flytta de värden som fanns ett snepp 
        pass 
    
    def popValue(self, index=-1):
        if self._data[index] != None: 
            self._data[index] = None 
            print(f"Value has been popped on index {index}")
        else: 
            print("there are is no value there to pop my friend")
        
    def removeValue(self, value=2):
        i = -1
        for a in self._data:
            i += 1
            if self._data[i] == value:
                print("wooo")
                self._data[i] = 0
                v = self._data[i+1]
                self._data[i] = v
                self._data[i+1] = 0 
                break
            else: 
                print("gay")
            
    def __str__(self): 
        # returns string representation of list, i.e [1, 2, 3]
        return f"{self._data}"
    
a = ArrayList()
a.appendValue(4)
a.appendValue(4)
a.appendValue(2)
a.appendValue(2)
print(a)

a.removeValue()
print(a)

