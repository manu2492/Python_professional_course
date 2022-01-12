x = int(input('choose a number'))
def is_prime(x):


    for i in range(2, x):
        if x % i == 0:
            return False 
        else:
            return True
def run():
    print(is_prime(x))

if __name__ == '__main__':
    run()
