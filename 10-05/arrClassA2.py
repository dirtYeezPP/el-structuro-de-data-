class Chonk:
    def __init__(self, initial_capacity=4):
        self._capacity = initial_capacity 
        self._size = 0 
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new = [None] * new_capacity 
        for i in range(self._size): 
            new[i] = self._data[i]
        self._data = new 
        self._capacity = new_capacity
    
    def yeet_in(self, value):
        if self._size == self._capacity: 
            self._resize(self._capacity * 2) 
            
        self._data[self._size] = value 
        self._size += 1 
    
    def peek(self, index):
        if index >= self._size: 
            raise IndexError("Missing correspondance of chonk level")
        
        return self._data[index]
    
    def scoot_over(self, index, value):
        
        if index > self._size: 
            raise IndexError("Missing correspondance of chonk level")
        
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        
        for j in range(self._size, index, -1):
            self._data[j] = self._data[j-1]
        self._data[index] = value 
        self._size += 1 
        return value

    
    def yoink(self, index=-1):
        if self._size == 0:
            raise IndexError("Nothing to yoink from Chonky list")
        if index == -1:
            index = self._size - 1 
        if index > self._size: 
            raise IndexError("Missing correspondance of Chonk level")

        yoinked = self._data[index]
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j+1]
            
        self._data[self._size - 1] = None
        self._size -= 1 
        
        if self._size > 0 and self._size <= self._capacity // 4: 
            self._resize(self._capacity//2)
         
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


print(a.chunk_level())
# print(a)

# a.chunk_level()
a.hunt_n_nuke(11)
print(a.is_chunky())
# print(a)

# a.yoink()
# print(a)
# a.yoink(1)
# print(a)

# a.scoot_over(2, 8)
# print(a)
