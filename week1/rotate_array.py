#rotate array by one

array = list(map(int, input("Enter the elements: ").split()))

if len(array) > 0:
    last = array[-1]

    
    for i in range(len(array) - 1, 0, -1):
        array[i] = array[i - 1]

    array[0] = last

print("Array after rotating by one:", array)
