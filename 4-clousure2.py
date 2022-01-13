word = input('please enter a dowrd')

times = int(input('please enter a number'))

def rep(word, times):

    response = word * times
    print(response)

rep(word, times)


#clousure version
def make_repeater_of(n):

    def repeater(string):
        return n * string

    return repeater

def run():

    repeat5 = make_repeater_of(5)
    print(repeat5('hi'))
run()


#clousure division

def make_division(n):

    def division(x):
        return x / n

    return division

def run():

    division5 = make_division(5)
    print(division5(10))

run()











