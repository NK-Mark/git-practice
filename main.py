# Test python env
def print_hello():
    animals = ['dog', 'cat', 'hamster', 'tiger']  # in one line
    foods = [
	'Spagetti',
	'Pizza',
	'bibimbab'
    ] # w/o trailing comma
    names = [
	'John',
	'Jane',
	'Gildong',
	'Dong-eun',
    ]  # w/ trailing comma 
    for f_name in names:
	print(f'hello, {f_name}')

if __name__ == '__main__':
    print_hello()
