mytuple = (1,2,3)

myit = iter(mytuple)


while True:
    try:
        element = next(myit)
        
        print(element)
        
    except StopIteration:
        break
        
