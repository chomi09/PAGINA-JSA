#print () #imprime text
#dir() #da informacion
#type() #te da que tipo es el dato

def hello(name='person'):
    print('Hello ' + name)
    
hello('joe')
hello()

# def add (n1, n2):
#     return n1 + n2
# print(add(22, 21))

print('-------------------------------')
add = lambda n1, n2: n1 + n2
print(add(8,3))