from memory_profiler import profile

@profile
def compute_squares(n):
    squares = [i * i for i in range(n)]
    return squares

if __name__ == '__main__':
    result = compute_squares(100000)
