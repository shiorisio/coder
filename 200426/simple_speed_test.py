import time
def time_test(func):
    def _time_test():
        a = time.time()
        func()
        return time.time() - a
    return _time_test

@time_test
def speed_test():
    for _ in range(10**10):
        pass

if __name__ == "__main__":
    print(speed_test())
