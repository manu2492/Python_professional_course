def fib(num):
    count = 0
    a1 = 0
    a2 = 1
    while count < num:
                
        ax = a1 + a2
        a1 = a2
        a2 = ax
        count += 1

        print(ax)

fib(5)

# iterators mode
class Fibolter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1 = self.n2
            self.n2 = self.aux
            return self.aux

if __name__ == '__main__':
    fibonacci = Fibolter() 
    for i in fibonacci:
        print(i)





