# Hashing functions
# creating a hash table using an array
# values are stored in an array of similar size

class HashTable:
    def __init__(self):
        self.size = 11 #array size
        self.key = [None]*self.size
        self.value = [None]*self.size

    def put(self, key, value):
        print('Inside put function')
        location = self.hashcode(key)
        if self.key[location] is None:
            self.key[location] = key
            self.value[location] = value
        else:
            if self.key[location] == key:
                self.value[location] = value

            else:
                rehashlocation = self.rehash(location)
                while self.key[rehashlocation] is not None and self.key[rehashlocation] != key:
                    rehashlocation = self.rehash(rehashlocation)

                if self.key[rehashlocation] is None:
                    self.key[rehashlocation] = key
                    self.value[rehashlocation] = value
                else:
                    if self.key[rehashlocation] == key:
                        self.value[rehashlocation] = value


    def get(self):
        #print('Inside get function')
        for i in range(self.size):
            print(self.key[i], self.value[i])

    def hashcode(self,key):
        #print('Get the hash code')
        return key%self.size

    def rehash(self, currenthashval):
        return (currenthashval + 1) % self.size

    def __getitem__(self):
        self.get()

    def __setitem__(self, key, value):
        self.put(key,value)


#main()
h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
h.get()



i = 5
j = i//2
print(j)
print(len([9,5,6,2,3]))