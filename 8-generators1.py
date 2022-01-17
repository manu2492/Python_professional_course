#a generator is a function that saves a state
#generator is better than iterator
import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            #yield pause the function state
            yield n1

        elif counter == 1:
            counter += 1
            yield n2

        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for i in fibonacci:
        print(i)
        time.sleep(1)



#challenge: stop the sequence in a given number
def fibo_gen2(stop: int):
    nn1 = 0
    nn2 = 1
    counter2 = 0

    while True:

        if counter2 == 0:
            counter2 += 1
            yield nn1

        elif counter2 == 1:
            counter2 += 1
            yield nn2

        else:
            aux2 = nn1 + nn2

            if not stop or aux2 <= stop:
                nn1, nn2 = nn2, aux2
                counter2 += 1
                yield aux2
            else:
                break


if __name__ == '__main__':
    fibonacci2 = fibo_gen2(5)

    for i in fibonacci2:
        print(i)
        time.sleep(1)





















