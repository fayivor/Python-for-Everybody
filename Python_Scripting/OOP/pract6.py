#MAking custom containers
class  TagCloud:
    def __init__(self):
        self.tags ={}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),0) + 1
    # Getting the item from the dictionary we use the __getitem__ magic method
    def __getitem__(self,tag):
        return self.tags.get(tag.lower(),0)
    #Setting the dictionary to a value we use the __setitem__ magic method
    # takes the key (tag) , value (count) pairs as parameters
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

   # To get the length of the dictionary we use the __len__ magic methods
    def __len__(self):
       return len(self.tags)

   # To make it iterable so we can iterate over it using a for loop we use
   # the __iter__ magic methods
    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud.add("Python")
cloud.add("Python")
cloud.add("python")
cloud.add("Python")
cloud.add("python")
print(cloud.tags)
cloud["python"]= 89
print(cloud.tags)
print(f"length of cloud object (dictionary) is {len(cloud)}")
print(iter(cloud.tags))
for i, l in iter(cloud.tags.items()):
    print(i,l)

for i, l in cloud.tags.items():
    print(i,l)
