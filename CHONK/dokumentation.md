# DOKUMENTATION OF THE CHONK LIST CLASS 
This documentation is for educational purposes only. 

## INIT ARGUMENTS 
###### CAPACITY 
The capacity of chonk is stored in the variable `self._capacity`, 
whereas creation requires an `initial capacity`, for the time being 
the initial capacity variable has a default value of 4. 

###### DATA 
`self._data` is the list in itself which initially has 4 reserved places in memory
that initially store the value `None`. 

###### SIZE 
`self._size` represents how many values or elements are actually 
stored within the chonk. As the data initially holds the value of `None`
on each index upon creation, the size is 0 and increments whenever 
elements or values are added. 

## INTERNAL FUNCTIONS 
### RESIZE 
``` py
def _resize(self, new_capacity):
    new = [None] * new_capacity 
    for i in range(self._size): 
        new[i] = self._data[i]
    self._data = new 
    self._capacity = new_capacity
```
The resize function is an internal function which is used in case 
a user wants to add values on indices that are out of bound usually (i.e
exceeding the capacity). 

The function requires an argument `new_capacity` in order 
to assign the `new` variable a list containing `None` on each index. 

The function then iterates through all elements in the list, 
so that the corresponding indices in `new` equal the values stored in `self._data`. 

The data is then assigned the new variable, meaning chonk gets a new capacity, 
and therefore more space to store future incoming values. 
The capacity of Chonk is also set to the new capacity. 

#### RESIZE TO BIGGER 
``` py
def _check_n_bulk(self):
    if self._size == self._capacity: 
        self._resize(self._capacity * 2)
        print("rawr")
```
This function checks whether the amount of elements is equal to 
the allowed capacity, in which case the `_resize` function is called to double 
the capacity of the current chonk. 

#### RESIZE TO SMALLER 
``` py
def _check_n_cut(self): 
    if self._size > 0 and self._size <= self._capacity // 4: 
        self._resize(self._capacity//2)
```
This function checks whether there are more than zero elements present 
and if the size is smaller or equal to the capacity divided by four. 
Both statements have to be true in order for the if-block to be executed. 

In the case where both statements are `True`, the `_resize` function 
is called as to lower the Chonk capacity by 50%. 

### INDEX CONTROL 
##### CHECKING INDEX 
``` py
def _check_chonk_index(self, index): 
    if index < 0: 
        index += self._size 
    if not (0 <= index < self._size): 
        raise IndexError("Chonk is not that Chonky")
    return index 
```
The function is responsible for converting a negative given index 
to math that the hardware can handle. 
In the case of a user giving the index -2 in a function such as 
`yoink`, this function will be called. The current size is then added onto the index
so that it mirrors the same index but in positive terms. 

The function later checks if the index is greater than or equal to zero and 
lesser than the current size (amount of present elements). 
In that case an IndexError is raised, to alert the user that the Index is out of
bounds. 
The index is then returned, as since it is an internal function 
the value needs to be returned for future usage purposes. 

### GET AND SET
The following functions allow the usage of `[]` when accessing a value 
or setting a value on a given index. 

##### GET ITEM 
``` py
def __getitem__(self, index):
    return self.spot(index)
```
This function allows for the syntax of `chonk[1]` when accessing a value at index 1, 
or any given index. 
The function calls `spot()` as to find and return the value of given index. 

##### SET ITEM
``` py 
def __setitem__(self, index, value):
    index = self._check_chonk_index(index)
    self._data[index] = value 
``` 
This function allows for a syntax as following: 
`chonk[2] = 'hello'` as to set a value on specified index. 
The function first makes sure the given index is of valid value and 
then sets the value on given index. 

##### LEN FUNCTION 
``` py 
def __len__(self):
    return self._size 
```
This function allows the syntax of `print(len(chonk))` 
for an output of the length of the list. 
In this case `self._size` is returned as it 
represents the amount of values/elements actually stored in chonk. 

## EXTERNAL FUNCTIONS 
### VIEWING OF VALUES 
Some functions only return a value, meaning that upon calling them 
it is necessary to do so inside `print()` as argument. 

##### PEEK FUNCTION
``` py
def peek(self):  
    return self._data[self._size - 1] 
```
The peek function is used in cases of stacking data structures 
to check the last value in the stack, without manipulating the data in any way. 
Some would explain it as *a pop that only returns the last value and does not delete it*.

##### SPOT FUNCTION 
``` py
def spot(self, index):
    index = self._check_chonk_index(index)
    print(self._data[index] if self._data[index] != None else 'No value on given index')
    return self._data[index]
```
The spot function is equivalent to a `get` function. 
The function first validates the given index after which it prints the value 
on given index, if the value is equal to `None` the *No value on given index* is printed 
out to the terminal. 
The value is then returned for the program's sake. 

### CHECKING FUNCTIONS 
##### IS CHUNKY FUNCTION 
``` py
def is_chunky(self):
    return self._size != 0
```
This function is reversed to what was wanted in the assignment 
as it returns `True` only when the size does not equal to zero. 
Whereas usually this function is used to check whether 
a list is empty or not, meaning it returns `True` when a list is empty. 

##### CHECKING SIZE OF CHONK 
``` py
def chunk_size(self):
    return self._size
```
This function returns the value stored within `self._size`. 

### APPENDING OF VALUES 
##### YEET IN / APPEND 
``` py
def yeet_in(self, value): 
    self._check_n_bulk()   

    self._data[self._size] = value 
    self._size += 1 
```
The function first checks whether there is enough space 
for another value to be added to chonk. 

Since size initially holds the value of 0, it mirrors 
the initial index of the chonk (or a list). 
As values are added, the size is incremented by one for each 
added value. 

This means that the size mirrors an empty spot no matter how many values 
are added. Indices start from 0, meaning that a list with 4 elements,  
has it's last value on index 3. The size therefore perfectly mirrors the empty spot at index 4. 

##### SCOOT OVER / INSERT 
``` py
def scoot_over(self, index, value):
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
```
This function is equivalent to `insert`. 
2 arguments are required for the function: index, and value, 
since the purpose is to insert a certain value at a certain index. 

First the function checks if the index is equal to `self._size` or 
if the given index is -1 (in which both indicate the last spot on the list). 
If it is, the `yeet_in()` function is called. After which the value is returned. 

The index is then validated and the capacity is checked. 

The function then performs a for-loop with the range starting at 
the value of `self._size`, ending at the value of the index, and stepping
the step of -1. 
Each value of the index is then moved one step to the right, in order to fit the 
given value at the index without overwriting the old. 


### DELETION OF VALUES 
##### YOINK 
The yoink function is equivalent to a `pop` function. 
``` py
def yoink(self, index=-1):
    if self._size == 0:
        raise IndexError("Nothing to yoink from Chonky list")
    if index == -1:
        index = self._size - 1 
    index = self._check_chonk_index(index)

    yoinked = self._data[index]
    for j in range(index, self._size - 1):
        self._data[j] = self._data[j+1]
            
    self._data[self._size - 1] = None 
    self._size -= 1 
        
    self._check_n_cut()
    return yoinked 
```
This function accepts an argument of given index if one is given, otherwise
it defaults to the index of -1. 

First the size is checked as so Chonk contains a value to delete. 
Otherwise an IndexError is raised. 

If the index is equal to -1, the user actually wants to 
delete an existent value in the list and not the actual last index in chonk. 
Therefore, the index is set to `self._size - 1`. 
In which the index is then validated by the `check_chonk_index` function. 

The targeted value is then stored in the variable `yoinked`. 
A for loop with a range is then executed, whereas this time 
the initial value is `index` and the ending value is `self._size - 1`. 

In this case, the remaining items are shifted one step to the left
to fill the gap left by the deleted value meaning that index 
has lost its value and needs to be overwritten. 

The following line: `self._data[self._size-1] = None` might seem optional, 
since `self._size -= 1` decrements the size by one, meaning that the value 
on the specified index will not be accessed either way. 
However, python cannot delete a value if it is not explicitly told to do so, 
meaning that the specified index has to get the value of `None` to free memory space. 

After decreasing the size, the function checks if chonk has to cut, 
as to not take up space for nothing. 

##### HUNT AND NUKE 
``` py
def hunt_n_nuke(self, value): 
    for i in range(self._size):
        if self._data[i] == value: 
            return self.yoink(i)
    print(f"Value {value} not found")
    return None 
```
The function accepts an argument containing the value which is 
wanted to be deleted. 
The size is then iterated through to check if an index is storing the 
specified value. 

If the value is present, the program uses the `yoink` function 
to delete the specified value at the specified and passed on index. 

Through `yoink` the size is decreased and the last index is set 
to hold the value of `None` for freeing up memory space. 

If no such value is found at any index, the program 
outputs *Value 5 not found* (if value = 5). 
The program then returns `None`. This is only for the program 
to know that it has nothing to hand back, in case the operation fails. 

## STR FUNCTION 
``` py
def __str__(self): 
    return f"{[self._data[i] for i in range(self._size)]}"
```
This function returns the values stored in `self._data` (or chonk 
so to speak) formatted as a list yes. Since the iteration is only 
executed in the range of the size, empty slots wont be outputted as 
`[None, None]`. 