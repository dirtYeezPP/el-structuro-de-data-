



``` py 
class ArrayList:
    def __init__(self, initial_capacity=4):
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity

    def _resolve_idx(self, index):
        # 1. If negative, add self._size
        # 2. Check bounds (0 <= index < self._size)
        # 3. Return positive index or raise IndexError
        pass

    def _bulk_up(self, new_capacity):
        # 1. Allocate new [None] * new_capacity
        # 2. Copy over 0 to self._size - 1
        # 3. Reassign self._data and self._capacity
        pass

    def cram(self, value):
        # 1. Check if full -> _bulk_up
        # 2. Place at self._size
        # 3. Increment self._size
        pass

    def peek(self, index):
        # 1. Use _resolve_idx
        # 2. Return value
        pass

    def scoot_and_stuff(self, index, value):
        # 1. Resolve index (allow index == self._size!)
        # 2. Check if full -> _bulk_up
        # 3. Shift backwards
        # 4. Insert and increment self._size
        pass

    def yoink(self, index=-1):
        # 1. Resolve index
        # 2. Save value
        # 3. Shift forwards
        # 4. Clear tail slot to None, decrement self._size
        # 5. Return saved value
        pass

    def __str__(self):
        # Return only the used portion: self._data[:self._size]
        return f"{[self._data[i] for i in range(self._size)]}"
```

``` py

class ArrayList: 
    def __init__(self, initial_capacity=6):
        self._capacity = initial_capacity
        self._size = 0 
        self._data = [None] * self._capacity
       
        
    def _resize(self, new_capacity):
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

```





``` py 
class Chonk:
    def __init__(self, initial_capacity=4):
        self._capacity = initial_capacity 
        self._size = 0 
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity
    
    def yeet_in(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
            
        self._data[self._size] = value 
        self._size += 1 
    
    def peek(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._data[index]
    
    def scoot_over(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")
            
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
            
        for j in range(self._size, index, -1):
            self._data[j] = self._data[j-1]
            
        self._data[index] = value 
        self._size += 1 
        return value
    
    def yoink(self, index=-1):
        if self._size == 0:
            raise IndexError("No chunk to yoink")
            
        if index == -1:
            index = self._size - 1 
            
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
            
        yoinked = self._data[index]
        
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j+1]
            
        self._data[self._size - 1] = None 
        self._size -= 1 
        
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
            
        return yoinked 
            
    def hunt_n_nuke(self, value):
        for i in range(self._size):
            if self._data[i] == value: 
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                self._data[self._size - 1] = None 
                self._size -= 1 
                return value 
        print(f"Value {value} not found")
        return None
                    
    def is_chunky(self):
        return self._size != 0
    
    def chunk_level(self):
        return self._size  
        
    def __str__(self): 
        return f"{[self._data[i] for i in range(self._size)]}"


a = Chonk()
a.yeet_in(2)
a.yeet_in(54)
a.yeet_in(9)
a.yeet_in(24)

a.chunk_level()
a.is_chunky()

print(a)
a.yeet_in(445)
a.yeet_in(134)

a.scoot_over(3, 88)
print(a)


a.yoink()
a.yoink(-2)
a.hunt_n_nuke(3)
print(a)

a.hunt_n_nuke(88)
a.yoink()
a.yoink()
print(a)
```