mytuple = {'a': 1, 'b': 2, 'c': 3}
myit = iter(mytuple.values())
myit2 = iter(mytuple)


while True:
    try:
        element = next(myit2)
        element2 = next(myit)
        
        print(element)
        print(element2)
        
        
       
        
    except StopIteration:
        break
