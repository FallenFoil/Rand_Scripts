import time
from functools import lru_cache


class withoutCache:
    def fib(self, number: int) -> int:
        if number == 0: return 0
        if number == 1: return 1
        return self.fib(number - 1) + self.fib(number - 2)

    def start(self):
        start = time.time()
        res = self.fib(40)
        print(f'Duration: {time.time() - start}s with result={res}')


class withCache:
    @lru_cache(maxsize=512)
    def fib(self, number: int) -> int:
        if number == 0: return 0
        if number == 1: return 1
        return self.fib(number - 1) + self.fib(number - 2)

    def start(self):
        start = time.time()
        res = self.fib(40)
        print(f'Duration: {time.time() - start}s with result={res}')


# Takes 56 seconds
withoutCache.start(withoutCache())
# Takes 0 seconds
withCache.start(withCache())