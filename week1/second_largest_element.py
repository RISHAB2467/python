#Find second largest element

array = list(map(int, input("Enter the elements: ").split()))


if len(array) < 2:
    print("Array must have at least two elements.")
else:
    largest = second_largest = float('-inf')

    for num in array:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("There is no second largest element (all elements may be equal).")
    else:
        print("The second largest element is:", second_largest)
