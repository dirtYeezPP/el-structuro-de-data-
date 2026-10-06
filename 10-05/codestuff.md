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

## AI HELP 
``` py
# alt 1
def appendValue(self, value):
        index = 0  # Start our manual index at 0
        
        for current_value in self._data:
            if current_value == None:  
                # We found an empty spot!
                self._data[index] = value 
                self._size += 1
                break  # Stop searching once we've appended
            
            # If it wasn't None, we move our manual index up by 1 and check the next item
            index += 1

# alt 2
def appendValue(self, value):
        # We can just jump directly to the first empty index using self._size!
        # (Assuming self._data still has empty None slots left)
        
        empty_index = self._size
        self._data[empty_index] = value
        self._size += 1


def removeValue(self, value):
        # 1. Loop only through the active elements
        for i in range(self._size):
            if self._data[i] == value:
                
                # 2. Shift ALL elements that come after 'i' one step to the left
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                
                # 3. Clear out the leftover duplicate at the very end of the active array
                self._data[self._size - 1] = None
                
                # 4. Decrease the size counter
                self._size -= 1
                
                print(f"Value {value} removed.")
                return # Exit the function completely since we found and removed it
        
        # If the loop finishes without hitting 'return', the value wasn't there
        print("Value not found in the list.")
```

## NOTES 

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
this works... it does, but uhm... i think there must be some 
better way of solving it. Right now im way too stubborn to 
ask AI however, so im just gonna roll with it. 


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
```