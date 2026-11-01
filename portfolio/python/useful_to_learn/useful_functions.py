#Go here for a complete list and for other functions: https://www.w3schools.com/python/python_ref_functions.asp

def tuples():
    print("Tuples.")
    print(tuple([1, 2, 3])) #Creates a tuple from a list.
    print(sum((1, 2, 3))) #Adds elements of an iterable.
    print(tuple(zip((1, 2, 3), (4, 5, 6)))) #Pairs first elements, then second elements, and so on. Use tuple to be able to display the result.
    print(tuple(map(sum, ((1, 2), (3, 4))))) #Does the same thing as the function below, except instead of being hardcoded to sum, it can do the same with any function.
    def mock_map(gtuple):
        rlist = []
        for i in gtuple:
            rlist.append(sum(i))
        return tuple(rlist)
    t = (1, 2, 3, 3)
    print(t.count(3)) #Returns the amount of times the specified value occurs in a tuple.
    print(t.index(2)) #Returns the index of the specified value in a tuple.
def lists():
    print("Lists.")
    l = [] #Initializes list with nothing in it.
    print(l)
    l.append(0) #Adds an element to the end of the list.
    print(l)
    l.extend([1, 2, 3]) #Extends the list by appending another list to it.
    print(l)
    l = l + [4, 5, 6] #Extends the list by appending another list to it.
    print(l)
    l.insert(4, 4) #Inserts an element specified by the second argument at the index specified by the first argument.
    print(l)
    print(l.index(5)) #Returns the index of the first element with the specified value.
    l.pop(4) #Removes the element at the specified index.
    print(l)
    l.remove(2) #Removes the element with the specified value.
    print(l)
    l.reverse() #Reverses the order of the list.
    print(l)
    l.sort() #Sorts the list.
    print(l)
def dicts():
    print("Dicts.")
    k = ("Jack", "John", "Bill", "James")
    v = ("Jefferson")
    d = dict.fromkeys(k, v) #Creates a dictionary where the same value is paired with each key.
    print(d)
    d.clear() #Clears evrything in a certain iterable.
    print(d)
    d.update({"Jack" : 2}) #Appends new dict to the dictionary.
    d.update({"John" : 12, "Bill" : 5, "James" : 19, "Max" : 14, "Grant" : 16})
    print(d)
    print(d.get("Bill")) #Returns the value that corresponds to the specified key.
    print(d.keys()) #Returns a list with the dictionaries keys in it.
    print(d.values()) #Returns a list with the dictionaries values in it.
    d.pop("Bill") #Removes the key-value pair with the given key.
    print(d)
    d.popitem() #Removes the last added key-value pair.
    print(d)
    print(d.setdefault("John", 13)) #Returns the value that corresponds to the specified key. If the key (argument 1) does not exist, the key and value(argument 2) will be appended to the dict.
tuples()
lists()
dicts()