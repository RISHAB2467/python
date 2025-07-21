#6. Check is array is sorted

array = list(map(int, input("Enter the elements: ").split()))

is_sorted = True

for i in range(1, len(array)):
    if array[i] < array[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print("The array is sorted in ascending order.")
else:
    print("The array is not sorted.")
