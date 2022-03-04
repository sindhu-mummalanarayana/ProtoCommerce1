class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__pop_Count = 0

    def get_counter(self):
        return self.__pop_Count

    def pop(self):
        self.__pop_Count += 1
        val = Stack.pop(self)

    def push(self, val):
        #self.__pop_Count += 1
        Stack.push(self, val)


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
