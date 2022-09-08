# https://docs.python.org/3/library/collections.html
from collections import Counter, OrderedDict, defaultdict, deque


# counter: counting hashable objects
print("Counter:")
counter = Counter(a=4, b=2, c=6, d=0, e=-2)
print(counter)
print(len(counter))
print(counter["b"])
print(list(counter.elements()))
print(counter.most_common())
counter.subtract(Counter(a=5, b=-3, c=1))
counter += Counter(a=2)  # add two counters (keep only positive counts)
print(counter)
# print(counter.total())  # since Python 3.10
print()

# namedtuple: replaced by dataclass since Python 3.7

# ordereddict: keeps the order of entries
print("OrderedDict:")
ordereddict = OrderedDict.fromkeys("cde")
print(ordereddict)
ordereddict["a"] = 1
ordereddict["f"] = 2
print(ordereddict)
print()

# defaultdict: calls factory function for missing values
print("Defaultdict:")
defdict = defaultdict(list)  # list default_factory
print(defdict)
# use default_factory methods (e.g. append for list)
defdict["a"].append(1)
defdict["b"].append(2)
defdict["a"].append(3)
defdict["c"] = 6  # can behave as regular dict
print(defdict)
print()

# deque: appends and pops on either end
print("Deque:")
deq = deque("bcd")
print(deq)
deq.append("a")
print(deq)
deq.appendleft("e")
print(deq)
deq.pop()
deq.popleft()
deq.extend("fg")
print(deq)
deq.rotate(2)  # rotate n steps to the right
print(deq)
