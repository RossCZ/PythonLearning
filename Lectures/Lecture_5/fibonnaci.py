n2 = 1
n1 = 1

for i in range(10):
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print(n2)
