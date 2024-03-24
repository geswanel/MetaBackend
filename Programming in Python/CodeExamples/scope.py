def a():
    animal = 'giraffe'

    def b():
        nonlocal animal
        animal = 'tiger'
        print('Inside nested function: ', animal)
    
    print('Before calling: ', animal)
    b()
    print('After calling: ', animal)


animal = 'Dog'
a()
print("In the global: ", animal)