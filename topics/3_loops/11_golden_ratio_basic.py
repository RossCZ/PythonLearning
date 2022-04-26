n2 = 1
n1 = 1

gr_previous = 0

for i in range(50):
    n3 = n2 + n1
    n1 = n2
    n2 = n3

    # golden ratio
    gr = n2 / n1
    print(f"golden ratio: {gr}")

    # difference
    diff = gr_previous - gr
    print(f"diff: {diff}")

    # update golden ratio
    gr_previous = gr

    # manually stop
    if abs(diff) < 0.01:
        break
