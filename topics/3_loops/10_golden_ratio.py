n2 = 1
n1 = 1

gr_previous = 0
gr = n2 / n1
diff = gr_previous - gr

while abs(diff) > 1e-9:
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
