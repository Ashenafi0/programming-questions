class Solution:
    def fib(self, n: int) -> int:
        def myfunc(no):
            if no==0:
                return 0
            if no==1:
                return 1
            cumulate=myfunc(no-1)+myfunc(no-2)
            return cumulate
        return myfunc(n)