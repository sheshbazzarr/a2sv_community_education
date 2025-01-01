class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values =[]

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val]=len(self.values)-1
        return True
       
    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # swap the elment to remove with the last elment
        last_element=self.values[-1]  #here you have the last elment 
        idx_to_remove = self.val_to_index[val] #tge
        self.values[idx_to_remove] =  last_element
        self.val_to_index[last_element]=idx_to_remove

        # remove the last element
        self.values.pop()
        del self.val_to_index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()