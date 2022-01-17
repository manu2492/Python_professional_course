# def a decorator function, it gets a fuction as a parameter
def upper_leters(func):
    
    #this function returns all upper letters 
    def envoltura(text):
        return func(text).upper()

    return envoltura

#this decorates what is bellow 
@upper_leters

def message(name):
    return f'{name}, you get a message'

print(message('cesar'))
#return: CESAR, YOU GET A MESSAGE

