# https://docs.python.org/3/library/itertools.html
import itertools
import operator


# infinite iterators
print("INFINITE ITERATORS")
print("Count")
for number in itertools.count(10, 10):
    if number == 40:
        break
    print(number, end=" ")

print("\nCycle")
for cycle_no, number in enumerate(itertools.cycle((0, 1)), start=1):
    if cycle_no == 6:
        break
    print(number, end=" ")

print("\nRepeat")
print(list(itertools.repeat("a", 5)))
print()

# terminating iterators
print("TERMINATING ITERATORS")
print("Accumulate")
print(list(itertools.accumulate([1, 2, 3, 4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))  # factorial!

print("Chain")
print(list(itertools.chain([1, 2, 3], [4, 5, 6], [7, 8], [9])))  # or from iterable (list of lists)

print("Compress")
print(list(itertools.compress("abeceda", [1, 1, 0, 1, 0, 1, 0])))

# ... dropwhile, filterfalse, groupby, islice, pairwise, starmap, takewhile, tee, zip_longest
print()

# combinatorics
print("COMBINATORICS")
print("Product")  # ~ nested for loop
print(list(itertools.product("abc", list(range(1, 4)))))

print("Permutations")
print(list(itertools.permutations("ABC", 2)))

print("Combinations")
print(list(itertools.combinations("ABC", 2)))

print("Combinations with replacement")
print(list(itertools.combinations_with_replacement("ABC", 2)))
