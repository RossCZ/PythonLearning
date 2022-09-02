import multiprocessing
import time


def is_prime_number(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False


def evaluate(n, multiprocess=False):
    start_num = 10000
    x_values = list(range(start_num, start_num + n))

    start = time.perf_counter()
    if multiprocess:
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = pool.map(is_prime_number, x_values)

        # another solution using apply async
        # processes = [pool.apply_async(is_prime_number, args=(x,)) for x in x_values]
        # results = [p.get() for p in processes]
    else:
        results = [is_prime_number(x) for x in x_values]
    print(f"Finished. Elapsed time: {(time.perf_counter() - start):.3f} s")


# all multiprocessing code must be guarded by __main__!
if __name__ == "__main__":
    # multiprocessing starts to be effective for more intensive calculations due to overhead with Pool creation
    n = 40000
    print("Single process:")
    evaluate(n, False)
    print("Multi process:")
    print(f"CPU count: {multiprocessing.cpu_count()}")
    evaluate(n, True)
