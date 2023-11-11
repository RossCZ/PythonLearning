import time
# computational complexity
# https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/
# https://www.freecodecamp.org/news/time-complexity-of-algorithms/
# space and time complexity
# https://en.wikipedia.org/wiki/Time_complexity
# https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
# https://medium.com/@stefentaime_10958/understanding-big-o-notation-with-real-world-python-examples-a4ed435b8a56


def constant_search(arr, searched_val):
    # O(1)
    inx = searched_val  # in case where array has same values as indices (starts at 0, ordered, values increment by 1)
    val = arr[inx]
    print("found", inx)
    return


def linear_search(arr, searched_val):
    # O(n)
    for i, val in enumerate(arr):
        if val == searched_val:
            print("found", i)
            return


def binary_search(arr, searched_val):
    #  O(log n)
    def get_mid_inx(inx_min, inx_max):
        return (inx_min + inx_max) // 2
    inx_max = len(arr) - 1
    inx_min = 0
    inx = get_mid_inx(inx_min, inx_max)

    while arr[inx] != searched_val:
        # print(inx, inx_min, inx_max)
        if arr[inx] > searched_val:  # result is on the left
            inx_max = inx - 1
        else:
            inx_min = inx + 1
        inx = get_mid_inx(inx_min, inx_max)
    print("found", inx)


def squared_search(arr, searched_val):
    # O(n^2) (bubble sort)
    # fabricated suboptimal algorithm
    for inx1, val in enumerate(arr):
        for inx2, val2 in enumerate(arr):  # unnecessary step (second iteration)
            if val == searched_val and val2 == searched_val:
                print("found", inx1, inx2)
                return


def search_example():
    arr = list(range(int(1e8)))

    print("starting search")
    start = time.time()
    # constant_search(arr, arr[-1])  # not limited by array size
    linear_search(arr, arr[-1])  # 1e8: 3s
    # binary_search(arr, arr[-1])  # 1e9: 7 ms
    # squared_search(arr, arr[-1])  # 1e4: 4s (!)
    end = time.time()
    print(f"elapsed time {(end - start) * 1000} ms")


def fibonacci_example():
    def naive_fibonacci(n):
        # O(2^n)
        global steps
        steps = steps + 1
        if n <= 1:
            return n
        else:
            return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

    n = 30
    result = naive_fibonacci(n)
    print(f"Result {result}; steps {steps:_}")  # 18m steps for n=34, 30m steps for n=35
    print(f"steps: n^3 {n ** 3:_}, 2^n: {2 ** n:_}")


# search_example()

steps = 0  # global variable
fibonacci_example()
