#functions
def say_hello():
    print('hello')
say_hello()
#parameters
def say_hello2(name,emoji):
    print(f'hello {name} {emoji}')
# positional arguments
say_hello2('Juan','*_*')

# keyword arguments
say_hello2(emoji='*_*',name='John')

#return

def uum(num1,num2):
   return num1+num2

# print(sum(int(input('choose a number')),int(input('choose another number'))))


#*args **kwargs
def super_func(*args,**kwargs):
    print(kwargs)
    total=0
    for items in kwargs.values():
        total += items
    return sum(args)+total

print(super_func(1,2,3,4,5,6,num5=5,num6=6))