import numpy as np
from timeit import default_timer as timer
from numba import vectorize

@vectorize(['float32(float32)'], target='cuda')
def pow(a):
    return a ** 3

def main():
    vec_size = 100000000

    a = b = np.array(np.random.sample(vec_size), dtype=np.float32)
    c = np.zeros(vec_size, dtype=np.float32)

    start = timer()
    c = pow(a)
    duration = timer() - start

    print(duration)

if __name__ == '__main__':
    main()
    size = 3
    print(np.array([1,2,3]))
    x = np.arange(size)
    y = np.arange(size)
    print(np.repeat(x, size))
    print(np.array([y]*size).flatten())

