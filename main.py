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
