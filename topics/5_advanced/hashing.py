print(hash(1))
print(hash("hello"))

# hash of immutable objects only
print(hash((1, "a")))

# error - hash of mutable objects not possible
# print(hash([1, 2]))
# print(hash({"a": 111}))


# hashable class
class Dog:
    def __init__(self, name, dog_id):
        self.name = name
        self.dog_id = dog_id

    # overriding methods __eq__ and __hash__ enables hashing
    # unique hash can be generated for each object to allow comparision
    def __eq__(self, other):
        return self.name == other.name and self.dog_id == other.dog_id

    def __hash__(self):
        return hash((self.name, self.dog_id))

    # overriding method __lt__ (and __eq__) enables sorting
    def __lt__(self, other):
        return self.dog_id < other.dog_id


print("Hashable class:")
dogs = {Dog("Ben", 2), Dog("Elf", 3), Dog("Doggo", 1), Dog("Dogecoin", 6)}
dogs.add(Dog("Doggo", 1))  # cannot be added - already in the list (by hash)

for d in sorted(dogs, reverse=False):
    print(f"{d.dog_id}: {d.name} (hash={hash(d)})")
