# ARRAY CLASS LIST IN PYTHON

## RULES 
you are not to use any of the following: 
* append(), insert(), pop(), remove(), extend(), clear(), index(), reverse() 
* del 
* Slicing (self._data[a:b]) 
* Konkatenering med + 
* Den inbyggda funktionen len() på self._data

### FURTHER INSTRUCTIONS 
1. `__init__(self, initial_capacity=4)` 
 * Skapar den interna listan self._data fylld med värdet None upp till initial_capacity. 
* Sätter self._capacity = initial_capacity. 
* Sätter self._size = 0. 
* _resize(self, new_capacity) (Intern hjälpmetod) 
* Skapar en ny intern lista av storleken new_capacity fylld med None. 
* Kopierar över alla self._size element från self._data till den nya listan med en loop. 
* Uppdaterar self._data och self._capacity. 

2. Grundläggande Metoder 
* append(value): Lägger till ett element sist i listan. Om self._size == self._capacity måste _resize(self._capacity * 2) anropas först. 
* get(index): Returnerar värdet på angivet index. Kasta IndexError("Index out of range") om indexet är ogiltigt (index < 0 eller index >= self._size). 
* set(index, value): Ändrar värdet på angivet index. Kasta IndexError vid ogiltigt index. 
* size(): Returnerar antalet element i listan (self._size). 
* is_empty(): Returnerar True om listan är tom, annars False. 

3. Förskjutning och Borttagning 
* insert(index, value): Sätter in ett värde på angiven position. Alla element från index och framåt måste förskjutas ett steg till höger. Om listan är full ska den förstoras först. 
* pop(index=-1): Tar bort och returnerar elementet på position index (standard är sista elementet -1). Elementen till höger om index måste förskjutas ett steg till vänster för att fylla hålet. 
* Optimering: Om self._size <= self._capacity // 4 och self._capacity > 4, halvera kapaciteten med _resize. 
* remove(value): Söker rätt på första förekomsten av value och tar bort det (använd gärna din pop-metod).  

## START CODE 
``` py
class ArrayList: 
	def __init__(self, initial_capacity=4): 
        self._capacity = initial_capacity 
    	self._size = 0 
    	# Skapa en intern lista med None av fast storlek 
    	self._data = [None] * self._capacity 
 
	def _resize(self, new_capacity): 
    	"""Intern metod för att ändra storlek på ”arrayen”.""" 
    	pass 
 
	def append(self, value): 
    	"""Lägger till ett element sist i listan.""" 
    	pass 
 
	def get(self, index): 
    	"""Hämtar element på angivet index.""" 
    	pass 
 
	def set(self, index, value): 
    	"""Ändrar element på angivet index.""" 
    	pass 
 
	def size(self): 
    	"""Returnerar antalet element i listan.""" 
    	pass 
 
	def is_empty(self): 
    	"""Returnerar True om listan är tom.""" 
    	pass 
 
	def insert(self, index, value): 
    	"""Sätter in ett element på angivet index.""" 
    	pass 
 
	def pop(self, index=-1): 
    	"""Tar bort och returnerar element på angivet index.""" 
    	pass 
 
	def remove(self, value): 
    	"""Tar bort första förekomsten av value.""" 
    	pass 
 
	def __str__(self): 
    	"""Returnerar strängrepresentation av listan, t.ex. '[1, 2, 3]'.""" 
    	pass 
```

## UTKAST AV KOD 
``` py
    def appendValue(self, value):
        for i in self._data:
            if self._data[i] == None:
                self._data[i] = value 
                i += 1
                print("aaa")
            elif self._data[i] != None:
                continue 
            else: 
                print("bbb")
                self._size += 1
                break 
        # print("bbb") 



                if empty_index == self._capacity: 
            print(self._data)
            print("cant add any more of those uncle")
        if self._size == self._capacity:
            print("the list has reached its limit")



	index = 0 
        for i in self._data: 
            if self._data[index] == value: 
                self._data[index] = self._data[-2]
                self._data[-2] = None 
                i += 1
                # index += 1
            else: 
                print("gaeee")
        # index += 1 
```


``` py
# a.appendValue(4)
# a.appendValue(5)
# a.appendValue(3)
# a.appendValue(4)
# print(a)
# a.appendValue(7) -> list reached limit yippie works 

# a.setValue(0, 9)

# print(a.ArrSize())
# print(a.getValue(0))
# print(a)
# print(a.Arr_is_empty())
# a.popValue()
# print(a)

# a.removeValue(5)
# print(a)
```

``` py
    def removeValue(self, value=2):
        i = 0
        for a in self._data:
            i += 1
            if self._data[i] == value:
                # i += 1
                print("wooo")
            else: 
                print("gay")
        i += 1
        a +=1 
```
why does that give me the desired output when it comes
across the values that match? 


``` py
    def removeValue(self, value=2):
        i = -1
        for a in self._data:
            i += 1
            if self._data[i] == value:
                # i += 1
                print("wooo")
            else: 
                print("gay")
        # i += 1
        # a +=1
```

``` py
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
```

``` py
    def removeValue(self, value):
        try: 
            i = -1
            for a in self._data:
                i += 1
                if self._data[i] == value:
                    print("wooo")
                    self._data[i] = None
                    v = self._data[i+1]
                    self._data[i] = v
                    self._data[i+1] = None
                    break
                else: 
                    print("gay")
        except: 
            print("nooooo") 

def removeValue(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                
                self._data[self._size - 1] = None
                self._size -= 1
                print(f"Value {value} removed.")
        print("Value not found in the list.")



    def insertValue(self, index, value):
        
        for i in range(self._size):
            if self._data[index] != None: 
                for j in range(i, self._size + 1):
                    self._data[j] = self._data[j-1]
                self._data[index] = value 
                self._size += 1
                print("im gay?")
                return 
            print("no youre gay")
        
        # inserts element in specific index 
        # 2. loopa igenom men byt värdet av det angivna indexet 
        # 3. flytta de värden som fanns ett snepp 

a.appendValue(4)
a.appendValue(4)
a.appendValue(2)
a.appendValue(2)
print(a)

a.removeValue(2)
print(a)

a.insertValue(1, 2)
print(a)
a.insertValue(2, 9)
print(a)



    def insertValue(self, index, value):
        for i in range(self._size):
            print("gg freaking ez")
            if self._data[i] != None: 
                for j in range(index, self._size + 1):
                    self._data[j] = self._data[j + 1]
                    
                self._data[index] = value
                self._size += 1
                print("im gay?")
                return 
            print("no you're gay")
        
        # inserts element in specific index 
        # 2. loopa igenom men byt värdet av det angivna indexet 
        # 3. flytta de värden som fanns ett snepp 


                for i in range(self._size):
            for j in range(i, self._size): 
                self._data[i] = self._data[i + 1]
                    
            self._data[index] = value
            self._size += 1
            print("im gay?")
            return 
        
        # inserts element in specific index 
        # 2. loopa igenom men byt värdet av det angivna indexet 
        # 3. flytta de värden som fanns ett snepp 

     
        # v = self._data[index] 
        # self._data[index+1] = v
        for j in range(index, self._size - 1):
            self._data[j + 1] = self._data[j] 
            # self._size += 1
            # j += 1
            
        self._data[index] = value 
        self._size += 1
```


``` py
def popValue(self, index=-1):
        if self._size == 0:
            print("There is no value there to pop my friend")

        if index == -1:
            index = self._size - 1

        if index < 0 or index >= self._size:
            print("Index gay")


        popped_value = self._data[index]
        for j in range(index, self._size - 1): 
            self._data[j] = self._data[j+1]

        self._data[self._size - 1] = None
        self._size -= 1 

        print(f"Value {popped_value} has been popped on index {index}")


        elif index != -1:
            index = index 
            if self._data[index] != None: 
                for j in range(index, self._size - 1): 
                    self._data[j] = self._data[j+1]
                self._data[self._size-1] = None
                self._size -= 1 
                print("gay111")
                return 
            else: 
                print("aaaaaaa")

    def insertValue(self, index, value):
        for i in range(self._capacity): 
            if i == index: 
                for j in range(i, self._size):
                    # self._data[j + 1] = self._data[j]
                    self._data[self._size] = self._data[j - 1]
                self._data[index] = value 
                self._size += 1
                print("gay")
                return 
        print("No") 
```


``` py 
        if self._size >= self._capacity: 
            print("arr full")
        
        if index > self._size: 
            print("invalid")
            
        for j in range(self._size, index, -1): 
            self._data[j] = self._data[j - 1]
            
        self._data[index] = value 
        self._size += 1 
        print(f"inserted {value} on index {index}")
```

``` py
if self._size == 0: 
            print("no values exist")
        if index == -1:
            index = self._size - 1 
        if index > self._size: 
            print("I like em big, i like me chönkeh")
        
        pv = self._data[index]
        for j in range(index, self._size - 1):
            self._data[j] = self._data[j + 1]
        
        self._data[self._size - 1] = None 
        self._size -= 1 
        
        print(f"value {pv} has been popped on index {index}")
         
```


``` py
        # internal method to change size of "array"
        # self._capacity = new_capacity
        newA = ArrayList(new_capacity)
        i = 0 
        for i in self._data:
            if self._data[i] != None: 
                newA.appendValue(self._data[i]) 
                # newA = self._data 
                i += 1
                if i == new_capacity: 
                    break 
            else: 
                newA[i] = 0 
```



``` py
class ArrayList:
    def __init__(self, initial_capacity=6):
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def appendValue(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def getValue(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def setValue(self, index, value):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        self._data[index] = value

    def ArrSize(self):
        return self._size

    def Arr_is_empty(self):
        return self._size == 0

    def insertValue(self, index, value):
        if not (0 <= index <= self._size):
            raise IndexError("Index out of bounds")

        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        for j in range(self._size, index, -1):
            self._data[j] = self._data[j - 1]

        self._data[index] = value
        self._size += 1

    def popValue(self, index=-1):
        if self._size == 0:
            raise IndexError("pop from empty list")

        if index == -1:
            index = self._size - 1

        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")

        removed_val = self._data[index]

        for j in range(index, self._size - 1):
            self._data[j] = self._data[j + 1]

        self._data[self._size - 1] = None
        self._size -= 1
        return removed_val

    def removeValue(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                self.popValue(i)
                return
        raise ValueError(f"{value} not in list")

    def __str__(self):
        # Displays only the active values
        return f"{[self._data[i] for i in range(self._size)]}"
```

``` py 
def getValue(self, index):
    index = self._normalize_index(index)
    return self._data[index]

def setValue(self, index, value):
    index = self._normalize_index(index)
    self._data[index] = value

def popValue(self, index=-1):
    if self._size == 0:
        raise IndexError("pop from empty list")
    
    # -1 automatically becomes self._size - 1
    index = self._normalize_index(index)
    
    removed_val = self._data[index]
    for j in range(index, self._size - 1):
        self._data[j] = self._data[j + 1]
        
    self._data[self._size - 1] = None
    self._size -= 1
    return removed_val
```

``` py 
def insertValue(self, index, value):
    # Convert negative index
    if index < 0:
        index += self._size

    # Valid insertion range is 0 to self._size inclusive
    if not (0 <= index <= self._size):
        raise IndexError("ArrayList insertion index out of range")

    if self._size == self._capacity:
        self._resize(2 * self._capacity)

    for j in range(self._size, index, -1):
        self._data[j] = self._data[j - 1]

    self._data[index] = value
    self._size += 1
```

