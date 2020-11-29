def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)


def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(num)
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)


def display(arr):
    for i in arr:
        print(i, end=" ")
    print("\n")


arr = []
while True:
    print("Select a choice\n")
    print("1.Insert\n2.Delete\n3.Display\n4.Quit")
    x = int(input())

    if(x == 1):
        t = int(input("Enter Value to insert:"))
        insert(arr, t)
    elif x == 2:
        t = int(input("Enter Value to insert:"))
        deleteNode(arr, t)
    elif x == 3:
        display(arr)
    else:
        break
    print("---------------------\n")


# insert(arr, 3)
# insert(arr, 4)
# insert(arr, 9)
# insert(arr, 5)
# insert(arr, 2)

# print("Max-Heap array: " + str(arr))

# deleteNode(arr, 4)
# print("After deleting an element: " + str(arr))
