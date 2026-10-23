class Chonk:
    def __init__(self, initial_capacity=4):
        self._capacity = self._check_cap(initial_capacity)
        # self._capacity = initial_capacity 
        self._size = 0 
        self._data = [None] * self._capacity

    def _check_cap(self, initial_capacity):
        # validate capacity of instance 
        if initial_capacity < 0: 
            print(f"Chonk cannot have the capacity of {initial_capacity}, the value will become positive.")
            initial_capacity = initial_capacity * -1 
        else: 
            self._capacity = initial_capacity 
        return initial_capacity 

    def _resize(self, new_capacity):
        # internal resize for future purposes 
        new = [None] * new_capacity 
        for i in range(self._size): 
            new[i] = self._data[i]
        self._data = new 
        self._capacity = new_capacity
        
    def _check_chonk_index(self, index): 
        # validate index value 
        if index < 0: 
            index += self._size 
        if not (0 <= index < self._size): 
            raise IndexError("Chonk is not that Chonky")
        return index 
        
    def _check_n_bulk(self):
        # check if the instance of class needs a bigger capacity 
        if self._size == self._capacity: 
            self._resize(self._capacity * 2)
            print("rawr")
             
    def _check_n_cut(self): 
        # check if the instance of class needs a smaller capacity 
        if self._size > 0 and self._size <= self._capacity // 4: 
            new_c = max(self._capacity // 2, 4)
            if new_c != self._capacity: 
                self._resize(self._capacity//2)
            
    def __getitem__(self, index):
        # function that allows for syntax with square brackets 
        return self.spot(index)
    
    def __setitem__(self, index, value):
        # function that allows for syntax with square brackets to set value 
        index = self._check_chonk_index(index)
        self._data[index] = value 
        
    def __len__(self):
        # function which allows for syntax of 'len(chonk)' 
        return self._size  

    def __add__(self, other:Chonk): # typed rawr
        # function which allows the instance to accept an argument of a list 
        new = Chonk()
        for i in range(self._size):
            new.yeet_in(self._data[i])
        for i in range(other._size):
            new.yeet_in(other._data[i])
        return new 

    def __del__(self): 
        print("Destructor called, instance deleted")
    
    def yeet_in(self, value):
        # append 
        self._check_n_bulk()
            
        self._data[self._size] = value 
        self._size += 1 
    
    def peek(self): 
        # peek 
        return self._data[self._size - 1] 
    
    def spot(self, index):
        # get 
        index = self._check_chonk_index(index)
        # print(self._data[index] if self._data[index] != None else 'No value on given index')
        return self._data[index]
    
    def scoot_over(self, index, value):
        # insert 
        if index == self._size or index == -1: 
            self.yeet_in(value)
            return value 
        
        index = self._check_chonk_index(index)
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
        index = self._check_chonk_index(index)

        yoinked = self._data[index]
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j+1]
            
        self._data[self._size - 1] = None 
        # logically this could be left out, since it wont be accessed 
        # however i wil leave it because i want infinite bum memory 
        # and because python is special 
        
        self._size -= 1 
        
        self._check_n_cut()
        return yoinked 
            
    def hunt_n_nuke(self, value):
        # remove 
        for i in range(self._size):
            if self._data[i] == value: 
                return self.yoink(i)
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
        # print 
        return f"{[self._data[i] for i in range(self._size)]}"
    

c = Chonk(-2)

print(c)
print(len(c))
# c.yoink(-1)

b = Chonk(4)
del b 