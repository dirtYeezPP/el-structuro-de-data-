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
        
    def _check_chonk_index(self, index): 
        if index > self._size: 
            raise IndexError("Missing correspondance of chonk level")
        
    def _check_n_bulk(self):
        if self._size == self._capacity: 
            self._resize(self._capacity * 2)
            print("rawr")
             
    def _check_n_cut(self): 
        if self._size > 0 and self._size <= self._capacity // 4: 
            self._resize(self._capacity//2)
            
    def __spillbeans(self, index):
        pass 
    
    def yeet_in(self, value):
        # append 
        self._check_n_bulk()
            
        self._data[self._size] = value 
        self._size += 1 
    
    def peek(self, index):
        # get 
        self._check_chonk_index(index)
        print(self._data[index] if self._data[index] != None else 'No value on given index')
        return self._data[index]
    
    def scoot_over(self, index, value):
        # insert 
        self._check_chonk_index(index)
        self._check_n_bulk()
        
        for j in range(self._size, index, -1):
            self._data[j] = self._data[j-1]
        self._data[index] = value 
        self._size += 1 
        return value

    def yoink(self, index=-1):
        # pop 
        if self._size == 0:
            raise IndexError("Nothing to yoink from Chonky list")
        if index == -1:
            index = self._size - 1 
        self._check_chonk_index(index)

        yoinked = self._data[index]
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j+1]
            
        # self._data[self._size - 1] = None 
        # eftersom vi utgår från size i andra ärenden
        # kommer vi inte komma åt denna oavsett
        # den kommer blir overridden vid kallelse på funktioner
        # som påverkar data... 
        self._size -= 1 
        
        self._check_n_cut()
        return yoinked 
            
    def hunt_n_nuke(self, value):
        # remove 
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
        # is empty 
        # print(True if self._size != 0 else False)
        # print(self._size != 0)
        return self._size != 0
    
    def chunk_size(self):
        # size 
        # print(self._size)
        return self._size  
        
    def __str__(self): 
        return f"{[self._data[i] for i in range(self._size)]}"
    

a = Chonk()
a.yeet_in(2)
a.yeet_in(54)
a.yeet_in(9)
a.yeet_in(24)

a.chunk_size()
a.is_chunky()

print(a)
a.yeet_in(445)
a.yeet_in(134)

a.scoot_over(3, 88)
print(a)


# a.yoink()
a.yoink(-2)
a.hunt_n_nuke(3)
print(a)

a.hunt_n_nuke(88)
# a.yoink()
a.yoink()
print(a)

print(a[2])


