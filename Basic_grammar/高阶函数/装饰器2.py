def log(text):
    def decorator(func):
        def weapper():
            print('{},{}'.format(text,func.__name__))
            return func()
        return weapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()