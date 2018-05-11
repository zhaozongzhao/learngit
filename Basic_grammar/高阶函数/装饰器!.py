def log(func):
    def wrapper(*args,**kw):
        print('call {}'.format(func.__name__))
        return func(*args,**kw)
    return  wrapper

@log
def now():
    print('1243325')

print(now())